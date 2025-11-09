# Contributing to Unified Biquaternion Theory

Thank you for your interest in contributing to UBT! This document provides guidelines for contributing to the repository.

## Ways to Contribute

### 1. Mathematical Rigor
- **Verify proofs**: Check existing derivations for errors
- **Complete gaps**: Address items in MATHEMATICAL_FOUNDATIONS_TODO.md
- **Formal proofs**: Add rigorous proofs where informal arguments exist
- **Independent verification**: Reproduce calculations independently

### 2. Numerical Calculations
- **Run existing scripts**: Verify predictions in `scripts/` directory
- **Extend calculations**: Add new predictions or higher precision
- **Optimization**: Improve computational efficiency
- **Visualization**: Create plots and figures for results

### 3. Literature Review
- **Find related work**: Identify similar approaches in literature
- **Add citations**: Contribute to LITERATURE_COMPARISON.md
- **Compare approaches**: Analyze differences with other theories
- **Historical context**: Document predecessors and inspirations

### 4. Documentation
- **Improve clarity**: Make technical content more accessible
- **Fix errors**: Correct typos, broken links, formatting
- **Add examples**: Provide worked examples for key concepts
- **Translations**: Translate documents (with author approval)

### 5. Critical Feedback
- **Identify problems**: Point out errors, inconsistencies, or gaps
- **Question assumptions**: Challenge unjustified claims
- **Suggest improvements**: Propose better approaches
- **Honest assessment**: Provide constructive criticism

## How to Contribute

### For Minor Changes (Typos, Small Fixes)
1. Fork the repository
2. Create a branch: `git checkout -b fix/description`
3. Make your changes
4. Commit: `git commit -m "Fix: description"`
5. Push and create a Pull Request

### For Major Changes (New Derivations, Calculations)
1. **Open an issue first** to discuss your proposal
2. Wait for feedback from maintainers
3. If approved, follow the fork-branch-PR workflow
4. Include:
   - Clear description of what you're adding
   - Motivation and context
   - References to related work
   - Tests/verification where applicable

### For Theoretical Contributions
1. **Discuss in GitHub Discussions or Issues first**
2. Provide mathematical details and references
3. Explain how it relates to existing UBT framework
4. Be prepared for critical review
5. Acknowledge uncertainties and limitations

## Contribution Standards

### Code Quality
- **Python**: Follow PEP 8 style guide
- **Documentation**: Add docstrings to all functions
- **Dependencies**: Minimize new dependencies
- **Testing**: Verify code produces correct results
- **Reproducibility**: Ensure others can run your code

### LaTeX Quality
- **Compilation**: Ensure documents compile without errors
- **Notation**: Follow existing notation conventions
- **References**: Use proper BibTeX citations
- **Clarity**: Write clear, well-structured content

### Scientific Integrity
- **Honesty**: Acknowledge limitations and uncertainties
- **Citations**: Credit all sources appropriately
- **Rigor**: Don't overstate confidence in results
- **Reproducibility**: Provide enough detail for verification
- **Categorization**: Label content per SPECULATIVE_VS_EMPIRICAL.md

### Content Categories
All contributions must be clearly categorized:
- 🟢 **EMPIRICAL**: Proven or experimentally validated
- 🟡 **SEMI-EMPIRICAL**: Mostly validated with acknowledged gaps
- 🔵 **THEORETICAL**: Framework established, predictions pending
- 🟠 **SPECULATIVE**: No quantitative predictions yet
- 🔴 **PHILOSOPHICAL**: Interpretation only

See SPECULATIVE_VS_EMPIRICAL.md for detailed guidelines.

## What We Welcome

✅ **Critical analysis** identifying errors or gaps  
✅ **Independent verification** of existing calculations  
✅ **Mathematical rigor** improvements  
✅ **Literature comparison** and proper citations  
✅ **Experimental proposals** with testable predictions  
✅ **Computational improvements** to existing scripts  
✅ **Documentation** clarifications  
✅ **Honest assessment** even if negative  

## What We Don't Accept

❌ **Unfalsifiable claims** without testable predictions  
❌ **Overstatement** of theory's status or maturity  
❌ **Pseudoscience** or claims contradicting established physics  
❌ **Plagiarism** or uncredited work  
❌ **Personal attacks** or disrespectful behavior  
❌ **Promotional content** unrelated to physics  

## Pull Request Process

### Before Submitting
1. **Read relevant documentation**: Understand existing framework
2. **Check for duplicates**: Ensure nobody else is working on it
3. **Test your changes**: Verify everything works
4. **Update documentation**: If you change functionality
5. **Follow style guidelines**: Match existing conventions

### PR Requirements
- Clear title describing the change
- Description explaining motivation and approach
- Reference to related issues (if any)
- Tests or verification of correctness
- No breaking changes without discussion

### Review Process
1. Maintainer will review your PR
2. May request changes or clarifications
3. Discussion may occur in PR comments
4. Once approved, will be merged
5. You'll be credited in commits and acknowledgments

## Collaboration Opportunities

### Current Priorities (see ROADMAP.md)
- **Phase 1 (Q4 2025 - Q2 2026)**: Mathematical foundations completion
- **Phase 2 (Q1 2026 - Q4 2026)**: Parameter derivations (B constant, hopfion coefficients)
- **Phase 3 (Q2 2026 - Q4 2026)**: Peer review paper preparation
- **Phase 4 (Q3 2026 - Q4 2027)**: Experimental predictions (CMB, dark matter)

### Skill-Specific Contributions

**Mathematicians:**
- Formalize inner product and integration measure
- Prove theorems rigorously
- Check for mathematical consistency

**Physicists:**
- Verify physical interpretations
- Calculate predictions
- Design experimental tests
- Compare to other theories

**Computational Scientists:**
- Optimize numerical calculations
- Parallelize computations
- Create visualization tools
- Improve code efficiency

**Technical Writers:**
- Improve documentation clarity
- Create tutorials and guides
- Write summaries for non-experts

## Issue and Discussion Guidelines

### Creating Issues

**Bug Reports:**
- Describe the problem clearly
- Provide steps to reproduce
- Include error messages or unexpected output
- Specify your environment (OS, Python version, etc.)

**Feature Requests:**
- Explain the proposed feature
- Justify why it's needed
- Discuss alternative approaches
- Be open to feedback

**Questions:**
- Check existing documentation first
- Be specific about what's unclear
- Provide context for your question

### Discussions
- Use GitHub Discussions for open-ended topics
- Keep discussions respectful and on-topic
- Back up claims with references or calculations
- Acknowledge when you're uncertain
- Be willing to change your mind based on evidence

## Recognition and Credit

### How Contributors Are Credited
- PR authors credited in Git history
- Significant contributors listed in acknowledgments
- Co-authorship on papers for substantial contributions
- Contributors may be mentioned in publications

### What Counts as "Substantial"
- Major mathematical derivations
- Significant code contributions
- Important error identification and fixes
- Extensive literature review work
- Experimental collaboration

## Communication

### Channels
- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Theoretical discussions, questions
- **Pull Requests**: Code/content contributions
- **Email**: For private matters (see README for contact)

### Response Time
- Maintainer typically responds within 1-2 weeks
- Complex PRs may take longer to review
- No response after 1 month? Feel free to ping

### Languages
- Primary: English (for broadest accessibility)
- Czech: Accepted for Czech-specific documents
- Other: Use English if possible, translations welcome

## Code of Conduct

See CODE_OF_CONDUCT.md for community standards.

**Summary:**
- Be respectful and professional
- Focus on ideas, not people
- Welcome diverse perspectives
- Prioritize scientific rigor and honesty

## Legal

### Licensing
- All contributions licensed under CC BY 4.0 (see LICENSE.md)
- By contributing, you agree to this license
- You retain copyright to your contributions
- Attribution will be preserved

### Attribution
- Always credit original authors
- Don't remove existing attributions
- Add your name to contributor lists appropriately

### Intellectual Property
- Don't contribute copyrighted material without permission
- If adapting published work, cite properly
- Original research contributions are encouraged

## Getting Started

### New Contributors
1. **Read**: README.md, OVERVIEW.md, UBT_READING_GUIDE.md
2. **Explore**: Review existing documents and code
3. **Identify**: Find an area where you can contribute
4. **Discuss**: Open an issue to propose your contribution
5. **Contribute**: Follow the PR process above

### First Contribution Ideas
- Fix typos or formatting in documentation
- Verify existing calculations in `scripts/`
- Add missing references to LITERATURE_COMPARISON.md
- Improve code documentation
- Create visualizations of results

### Advanced Contributions
- Complete items in MATHEMATICAL_FOUNDATIONS_TODO.md
- Implement ROADMAP.md milestones
- Derive fitted parameters from first principles
- Calculate new testable predictions

## Questions?

- **Technical questions**: Open a GitHub Discussion
- **Contribution process**: Open an issue asking for clarification
- **Private matters**: Email (see README for contact info)

---

**Thank you for contributing to UBT!**

Whether you're fixing a typo, verifying a calculation, or contributing a major derivation, every contribution helps advance our understanding of fundamental physics.

Remember: Science progresses through collaboration, critical thinking, and honest evaluation. Your contributions—positive or negative—are valued.

---

**Document Status:** Living document  
**Last Updated:** November 5, 2025  
**Maintained by:** David Jaroš and UBT community
