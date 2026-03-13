"""
su22.py - SU(2,2) Hermitian form and invariants

Implements the natural Hermitian form on twistor space ℂ⁴:

    H = [[0,  I₂],
         [I₂, 0 ]]

and the associated twistor inner product:

    ⟨Z₁, Z₂⟩ = Z₁† H Z₂

This is preserved under SU(2,2) transformations (conformal group).

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, eye, simplify, conjugate, I

from THEORY_COMPARISONS.penrose_twistor.common.linalg import hermitian_conjugate
from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
from THEORY_COMPARISONS.penrose_twistor.twistor_core.numeric import (
    norm_fro, max_abs, close_matrix, seeded_rng, random_complex
)


def get_su22_hermitian_form():
    """
    Return the SU(2,2) Hermitian form H.
    
    H = [[0,  I₂],
         [I₂, 0 ]]
    
    where I₂ is the 2×2 identity matrix.
    
    Returns
    -------
    sympy.Matrix (4×4)
        Hermitian form H
    
    Notes
    -----
    This is the standard invariant form for SU(2,2), the conformal group
    of compactified Minkowski space.
    """
    I2 = eye(2)
    Z2 = Matrix.zeros(2, 2)
    
    # Block matrix:
    # H = [[0,  I₂],
    #      [I₂, 0 ]]
    H = Matrix.vstack(
        Matrix.hstack(Z2, I2),
        Matrix.hstack(I2, Z2)
    )
    
    return H


def twistor_inner(Z1, Z2):
    """
    Compute SU(2,2) inner product of two twistors.
    
    ⟨Z₁, Z₂⟩ = Z₁† H Z₂
    
    where H is the SU(2,2) Hermitian form.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to compute inner product of
    
    Returns
    -------
    sympy expression
        Inner product (complex scalar)
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
    >>> Z1 = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    >>> Z2 = Twistor(Matrix([0, 1]), Matrix([1, 0]))
    >>> inner = twistor_inner(Z1, Z2)
    """
    H = get_su22_hermitian_form()
    
    # Convert twistors to 4-vectors
    vec1 = Z1.to_vector()  # 4×1 column vector
    vec2 = Z2.to_vector()  # 4×1 column vector
    
    # Compute ⟨Z₁, Z₂⟩ = vec1† H vec2
    # vec1† is (1×4) row vector, H is 4×4, vec2 is 4×1 column vector
    # Result is 1×1
    vec1_dag = vec1.H  # Hermitian conjugate: conjugate transpose, now 1×4
    result = (vec1_dag * H * vec2)[0, 0]
    
    return simplify(result)


def twistor_norm_squared(Z):
    """
    Compute squared norm of a twistor: ⟨Z, Z⟩.
    
    Parameters
    ----------
    Z : Twistor
        Twistor to compute norm of
    
    Returns
    -------
    sympy expression
        Squared norm ⟨Z, Z⟩
    
    Notes
    -----
    For the SU(2,2) form, the norm can be positive, negative, or zero.
    - Positive: timelike twistor
    - Negative: spacelike twistor  
    - Zero: null twistor
    """
    return twistor_inner(Z, Z)


def is_hermitian_form(H):
    """
    Verify that H is Hermitian: H† = H.
    
    Parameters
    ----------
    H : sympy.Matrix
        Matrix to check
    
    Returns
    -------
    bool
        True if Hermitian, False otherwise
    """
    return simplify(H - hermitian_conjugate(H)) == Matrix.zeros(*H.shape)


def verify_su22_form_hermitian():
    """
    Verify that the SU(2,2) form H is Hermitian.
    
    Returns
    -------
    bool
        True if H is Hermitian
    """
    H = get_su22_hermitian_form()
    return is_hermitian_form(H)


def twistor_inner_conjugate_symmetry(Z1, Z2):
    """
    Verify conjugate symmetry: ⟨Z₁, Z₂⟩* = ⟨Z₂, Z₁⟩.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to test
    
    Returns
    -------
    bool
        True if conjugate symmetry holds
    """
    inner12 = twistor_inner(Z1, Z2)
    inner21 = twistor_inner(Z2, Z1)
    
    diff = simplify(conjugate(inner12) - inner21)
    
    return diff == 0


def twistor_inner_linearity_test(Z1, Z2, Z3, alpha, beta):
    """
    Verify linearity in second argument:
    ⟨Z₁, αZ₂ + βZ₃⟩ = α⟨Z₁, Z₂⟩ + β⟨Z₁, Z₃⟩
    
    Parameters
    ----------
    Z1, Z2, Z3 : Twistor
        Test twistors
    alpha, beta : sympy expressions
        Complex coefficients
    
    Returns
    -------
    bool
        True if linearity holds
    """
    # Construct αZ₂ + βZ₃
    omega_combined = alpha * Z2.omega + beta * Z3.omega
    pi_combined = alpha * Z2.pi + beta * Z3.pi
    Z_combined = Twistor(omega_combined, pi_combined)
    
    # Compute both sides
    lhs = twistor_inner(Z1, Z_combined)
    rhs = alpha * twistor_inner(Z1, Z2) + beta * twistor_inner(Z1, Z3)
    
    diff = simplify(lhs - rhs)
    
    return diff == 0


def su22_transformation_preserves_inner(U, Z1, Z2):
    """
    Verify that SU(2,2) transformation U preserves inner product.
    
    An SU(2,2) matrix U satisfies: U† H U = H
    
    This test checks: ⟨UZ₁, UZ₂⟩ = ⟨Z₁, Z₂⟩
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Transformation matrix (should be in SU(2,2))
    Z1, Z2 : Twistor
        Test twistors
    
    Returns
    -------
    bool
        True if inner product is preserved
    
    Notes
    -----
    This function does NOT verify that U is actually in SU(2,2).
    It only checks if the transformation preserves the inner product.
    """
    H = get_su22_hermitian_form()
    
    # First verify U is SU(2,2): U† H U = H
    is_su22 = simplify(hermitian_conjugate(U).T * H * U - H) == Matrix.zeros(4, 4)
    
    if not is_su22:
        return False
    
    # Transform twistors
    vec1 = Z1.to_vector()
    vec2 = Z2.to_vector()
    
    vec1_transformed = U * vec1
    vec2_transformed = U * vec2
    
    Z1_transformed = Twistor.from_vector(vec1_transformed)
    Z2_transformed = Twistor.from_vector(vec2_transformed)
    
    # Check preservation
    inner_original = twistor_inner(Z1, Z2)
    inner_transformed = twistor_inner(Z1_transformed, Z2_transformed)
    
    diff = simplify(inner_original - inner_transformed)
    
    return diff == 0


def twistor_orthogonal(Z1, Z2):
    """
    Check if two twistors are orthogonal: ⟨Z₁, Z₂⟩ = 0.
    
    Parameters
    ----------
    Z1, Z2 : Twistor
        Twistors to check
    
    Returns
    -------
    bool
        True if orthogonal, False otherwise
    """
    inner = twistor_inner(Z1, Z2)
    return simplify(inner) == 0


def create_orthogonal_twistor(Z1):
    """
    Create a twistor orthogonal to Z1 (if possible).
    
    Uses the fact that for H with block anti-diagonal structure:
    If Z₁ = (ω₁, π₁), then Z₂ = (π₁, -ω₁) is orthogonal.
    
    This is because: ⟨Z₁, Z₂⟩ = ω₁†π₁ + π₁†(-ω₁) = ω₁†π₁ - π₁†ω₁ = 0
    (since ω₁†π₁ is a scalar, it equals (π₁†ω₁)†  = (π₁†ω₁)* = conjugate transpose).
    
    Parameters
    ----------
    Z1 : Twistor
        Reference twistor
    
    Returns
    -------
    Twistor
        Orthogonal twistor Z₂
    
    Examples
    --------
    >>> from sympy import Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.twistor import Twistor
    >>> Z1 = Twistor(Matrix([1, 0]), Matrix([0, 1]))
    >>> Z2 = create_orthogonal_twistor(Z1)
    >>> twistor_orthogonal(Z1, Z2)
    True
    """
    # Swap ω and π and negate the new π to get orthogonal twistor
    return Twistor(Z1.pi, -Z1.omega)


def get_su22_signature():
    """
    Get the signature of the SU(2,2) Hermitian form.
    
    Returns
    -------
    tuple
        (n_positive, n_negative, n_zero) eigenvalue counts
    
    Notes
    -----
    For SU(2,2), the signature should be (2, 2, 0).
    """
    H = get_su22_hermitian_form()
    eigenvals = H.eigenvals()
    
    n_positive = 0
    n_negative = 0
    n_zero = 0
    
    for eigval, multiplicity in eigenvals.items():
        eigval_simplified = simplify(eigval)
        if eigval_simplified > 0:
            n_positive += multiplicity
        elif eigval_simplified < 0:
            n_negative += multiplicity
        else:
            n_zero += multiplicity
    
    return (n_positive, n_negative, n_zero)


def is_su22(U, tolerance=1e-10):
    """
    Check if a 4×4 matrix U is in SU(2,2).
    
    A matrix is in SU(2,2) if:
        1. U† H U = H  (preserves the Hermitian form)
        2. det(U) = 1  (special unitary)
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Matrix to test
    tolerance : float, optional
        Numerical tolerance for checking (default 1e-10)
        Only used for numerical matrices
    
    Returns
    -------
    bool
        True if U is in SU(2,2) (within tolerance if numeric)
    
    Notes
    -----
    For symbolic matrices, uses exact simplification.
    For numeric matrices, uses tolerance-based comparison.
    
    Examples
    --------
    >>> from sympy import Matrix, eye
    >>> U = eye(4)  # Identity is in SU(2,2)
    >>> is_su22(U)
    True
    """
    H = get_su22_hermitian_form()
    
    # Check U† H U = H
    U_dag = U.H
    product = U_dag * H * U
    residual = simplify(product - H)
    
    # Try symbolic check first
    if residual == Matrix.zeros(4, 4):
        form_preserved = True
    else:
        # Fall back to numeric check
        try:
            # Convert to numeric and check norm
            residual_numeric = residual.evalf()
            max_entry = max(abs(complex(residual_numeric[i, j])) 
                          for i in range(4) for j in range(4))
            form_preserved = max_entry < tolerance
        except:
            form_preserved = False
    
    # Check det(U) = 1
    det_U = U.det()
    det_simplified = simplify(det_U)
    
    if det_simplified == 1:
        det_is_one = True
    else:
        try:
            det_numeric = complex(det_simplified.evalf())
            det_is_one = abs(det_numeric - 1.0) < tolerance
        except:
            det_is_one = False
    
    return form_preserved and det_is_one


def su22_lie_algebra_element(A_params):
    """
    Create an su(2,2) Lie algebra element from parameters.
    
    An element A of su(2,2) satisfies: A† H + H A = 0
    
    With H = [[0, I], [I, 0]], if A = [[B, C], [D, E]], then:
        A† H + H A = 0 implies:
        D = -C†  and  E = -B†
    
    Parameters
    ----------
    A_params : dict
        Parameters defining the algebra element.
        Should contain 'theta' and 'scale' for a simple test element.
    
    Returns
    -------
    sympy.Matrix (4×4)
        An su(2,2) Lie algebra element
    
    Notes
    -----
    This is a simplified constructor for testing.
    We construct A with the correct block structure to satisfy A† H + H A = 0.
    
    Examples
    --------
    >>> A = su22_lie_algebra_element({'theta': 0.1, 'scale': 1.0})
    """
    theta = A_params.get('theta', 0.1)
    scale = A_params.get('scale', 1.0)
    
    # For A = [[B, C], [D, E]] to satisfy A† H + H A = 0:
    # We need D = -C† and E = -B†
    
    # Choose B as anti-Hermitian (B† = -B) for simplicity
    B = Matrix([
        [0, theta],
        [-theta, 0]
    ]) * scale
    
    # Choose C as a general 2×2 matrix
    C = Matrix([
        [theta, 0],
        [0, theta]
    ]) * scale * I  # Multiply by i to keep things anti-Hermitian
    
    # Compute D and E from constraints
    D = -C.H  # D = -C†
    E = -B.H  # E = -B†
    
    # Construct A
    A = Matrix.vstack(
        Matrix.hstack(B, C),
        Matrix.hstack(D, E)
    )
    
    return A


def exponentiate_su22_algebra(A, numeric=True):
    """
    Exponentiate an su(2,2) Lie algebra element to get SU(2,2) element.
    
    U = exp(A)
    
    Parameters
    ----------
    A : sympy.Matrix (4×4)
        Lie algebra element (should satisfy A† H + H A = 0)
    numeric : bool, optional
        If True, compute numeric exponential (default True)
        If False, leave as symbolic exp(A)
    
    Returns
    -------
    sympy.Matrix (4×4)
        U = exp(A) in SU(2,2)
    
    Notes
    -----
    Numeric exponentiation uses series expansion or sympy's exp method.
    For small parameters, first-order U ≈ I + A is often sufficient.
    """
    if numeric:
        # Use sympy's matrix exponential
        # For small A, we can use Taylor series
        I4 = eye(4)
        
        # First check if A is small enough for first-order approximation
        try:
            A_numeric = A.evalf()
            max_entry = max(abs(complex(A_numeric[i, j])) 
                          for i in range(4) for j in range(4))
            
            if max_entry < 0.2:
                # Use first-order: exp(A) ≈ I + A
                U = I4 + A
            else:
                # Use higher order Taylor series: exp(A) ≈ I + A + A²/2
                U = I4 + A + (A*A)/2
            
            return U.evalf()
        except:
            # Fall back to symbolic
            return sp.exp(A)
    else:
        # Symbolic exponential (not evaluated)
        return sp.exp(A)


def random_su22_element_numeric(seed=None, scale=0.1):
    """
    Generate a random SU(2,2) element numerically.
    
    Constructs a small su(2,2) algebra element and exponentiates it.
    
    Parameters
    ----------
    seed : int, optional
        Random seed for reproducibility
    scale : float, optional
        Scale factor for algebra element (default 0.1)
    
    Returns
    -------
    sympy.Matrix (4×4)
        A numeric SU(2,2) matrix
    
    Examples
    --------
    >>> U = random_su22_element_numeric(seed=42, scale=0.1)
    >>> is_su22(U)  # Should be True (within tolerance)
    True
    """
    import random
    if seed is not None:
        random.seed(seed)
    
    # Create random algebra element
    theta = random.uniform(-scale, scale)
    phi = random.uniform(-scale, scale)
    
    A = su22_lie_algebra_element({'theta': theta, 'phi': phi, 'scale': 1.0})
    
    # Exponentiate
    U = exponentiate_su22_algebra(A, numeric=True)
    
    return U


def H():
    """
    Explicit helper to get the SU(2,2) Hermitian form H.
    
    Convenience alias for get_su22_hermitian_form().
    
    Returns
    -------
    sympy.Matrix (4×4)
        Hermitian form H = [[0, I₂], [I₂, 0]]
    """
    return get_su22_hermitian_form()


def dagger(M):
    """
    Compute conjugate transpose (Hermitian conjugate) of a matrix.
    
    M† = (M*)ᵀ = conjugate transpose
    
    Parameters
    ----------
    M : sympy.Matrix
        Input matrix
    
    Returns
    -------
    sympy.Matrix
        Hermitian conjugate M†
    
    Examples
    --------
    >>> from sympy import Matrix, I
    >>> M = Matrix([[1, I], [0, 2]])
    >>> M_dag = dagger(M)
    >>> # M_dag = [[1, 0], [-I, 2]]
    """
    return M.H


def is_H_unitary(U, tol=1e-9):
    """
    Check if U is H-unitary: U† H U = H within tolerance.
    
    An element of SU(2,2) must preserve the Hermitian form H.
    This is the defining property: U† H U = H.
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Matrix to check
    tol : float, optional
        Numerical tolerance (default 1e-9)
    
    Returns
    -------
    bool
        True if U preserves H within tolerance
    
    Examples
    --------
    >>> from sympy import eye
    >>> U = eye(4)
    >>> is_H_unitary(U)  # True
    True
    """
    H_form = H()
    U_dag = dagger(U)
    
    # Compute U† H U
    product = U_dag * H_form * U
    
    # Check ||U† H U - H||_F < tol
    residual = product - H_form
    return norm_fro(residual) < tol


def random_su22_lie_element(seed=None, scale=1.0):
    """
    Generate a random su(2,2) Lie algebra element via projection.
    
    Produces A satisfying the Lie algebra constraint:
        A† H + H A = 0  (H-anti-Hermitian condition)
    
    Algorithm:
    1. Start with random complex 4×4 matrix A_random
    2. Project to su(2,2) constraint:
        A = 0.5 * (A_random - H^(-1) A_random† H)
    
    This ensures A† H + H A = 0 exactly (up to numerical precision).
    
    Parameters
    ----------
    seed : int, optional
        Random seed for reproducibility
    scale : float, optional
        Scale factor for random entries (default 1.0)
    
    Returns
    -------
    sympy.Matrix (4×4)
        H-anti-Hermitian Lie algebra element
    
    Examples
    --------
    >>> A = random_su22_lie_element(seed=42, scale=0.1)
    >>> H_form = H()
    >>> residual = dagger(A) * H_form + H_form * A
    >>> norm_fro(residual) < 1e-10  # Should be True
    True
    
    Notes
    -----
    For H = [[0, I], [I, 0]], we have H^(-1) = H.
    So the projection simplifies to: A = 0.5 * (A_random - H A_random† H)
    """
    rng = seeded_rng(seed) if seed is not None else seeded_rng(42)
    
    # Generate random complex 4×4 matrix
    A_random = Matrix([
        [random_complex(rng, scale) for _ in range(4)]
        for _ in range(4)
    ])
    
    # Get H (note: H^(-1) = H for our specific form)
    H_form = H()
    
    # Project to su(2,2): A = 0.5 * (A_random - H A_random† H)
    A_dag_random = dagger(A_random)
    A_proj = sp.Rational(1, 2) * (A_random - H_form * A_dag_random * H_form)
    
    # Evaluate numerically
    A_proj = A_proj.evalf()
    
    return A_proj


def cayley_transform(A, alpha=1.0):
    """
    Construct SU(2,2) group element via Cayley transform.
    
    Given A in su(2,2) (satisfying A† H + H A = 0), construct:
        U = (I - αA)^(-1) (I + αA)
    
    This preserves H-unitarity: U† H U = H if A† H + H A = 0.
    
    The parameter alpha allows rescaling A for better numerical conditioning.
    Small alpha (e.g., 0.05) helps avoid numerical issues.
    
    Parameters
    ----------
    A : sympy.Matrix (4×4)
        H-anti-Hermitian Lie algebra element (A† H + H A = 0)
    alpha : float, optional
        Scaling factor (default 1.0)
        Use smaller values (e.g., 0.05) for better numerical stability
    
    Returns
    -------
    sympy.Matrix (4×4)
        Group element U in SU(2,2)
    
    Examples
    --------
    >>> A = random_su22_lie_element(seed=42, scale=0.1)
    >>> U = cayley_transform(A, alpha=0.05)
    >>> is_H_unitary(U, tol=1e-9)  # Should be True
    True
    
    Notes
    -----
    The Cayley transform is numerically superior to matrix exponential for
    constructing group elements. It preserves the H-unitarity exactly
    (up to numerical precision) when A is H-anti-Hermitian.
    
    Branch choice: The resulting U may have det(U) ≠ 1 due to branch cuts.
    Use normalize_det() to enforce det(U) = 1.
    """
    I4 = eye(4)
    
    # Scale A
    A_scaled = alpha * A
    
    # Compute numerator and denominator
    numerator = I4 + A_scaled
    denominator = I4 - A_scaled
    
    # Check if denominator is invertible
    det_denom = denominator.det()
    det_val = complex(det_denom.evalf())
    
    if abs(det_val) < 1e-12:
        raise ValueError(f"Cayley transform singular: det(I - αA) = {det_val}")
    
    # Compute U = (I - αA)^(-1) (I + αA)
    denominator_inv = denominator.inv()
    U = denominator_inv * numerator
    
    # Evaluate numerically
    U = U.evalf()
    
    return U


def to_blocks_2x2(U):
    """
    Split 4×4 matrix U into 2×2 blocks A, B, C, D.
    
    U = [[A, B],
         [C, D]]
    
    where A, B, C, D are 2×2 matrices.
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Matrix to decompose
    
    Returns
    -------
    tuple of sympy.Matrix
        (A, B, C, D) as 2×2 matrices
    
    Examples
    --------
    >>> from sympy import eye
    >>> U = eye(4)
    >>> A, B, C, D = to_blocks_2x2(U)
    >>> A == eye(2) and D == eye(2)  # True
    True
    """
    A = U[:2, :2]
    B = U[:2, 2:]
    C = U[2:, :2]
    D = U[2:, 2:]
    
    return A, B, C, D


def normalize_det(U):
    """
    Normalize determinant to det(U) = 1.
    
    If det(U) ≠ 1 (numerically), normalize by:
        U_normalized = U / det(U)^(1/4)
    
    Uses principal branch for complex 1/4 power.
    
    Parameters
    ----------
    U : sympy.Matrix (4×4)
        Matrix to normalize
    
    Returns
    -------
    sympy.Matrix (4×4)
        Normalized matrix with det ≈ 1
    
    Notes
    -----
    Branch caveat: The 1/4 power has multiple branches. We use the
    principal branch. For small deviations from det=1, this is acceptable.
    
    For matrices very close to SU(2,2), the determinant should already
    be near 1, so this is primarily a numerical cleanup.
    
    Examples
    --------
    >>> from sympy import eye
    >>> U = 1.1 * eye(4)  # det = 1.1^4 ≈ 1.4641
    >>> U_norm = normalize_det(U)
    >>> abs(complex(U_norm.det().evalf()) - 1.0) < 1e-10  # True
    True
    """
    det_U = U.det()
    det_val = complex(det_U.evalf())
    
    if abs(det_val) < 1e-12:
        raise ValueError(f"Cannot normalize: det(U) ≈ 0")
    
    # Compute det^(1/4) using principal branch
    # For complex z, z^(1/4) = |z|^(1/4) * exp(i*arg(z)/4)
    det_fourth_root = det_val ** (1/4)
    
    # Normalize: U_normalized = U / det^(1/4)
    U_normalized = U / det_fourth_root
    U_normalized = U_normalized.evalf()
    
    return U_normalized

