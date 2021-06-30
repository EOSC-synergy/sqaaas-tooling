# Approval process for new tools 
As commented several times throughout the present documentation, the SQAaaS platform is compliant with the following criteria:
- [A set of Common Software Quality Assurance Baseline Criteria for Research Projects](https://indigo-dc.github.io/sqa-baseline/)
- [A set of Common Service Quality Assurance Baseline Criteria for Research Projects](https://eosc-synergy.github.io/service-qa-baseline/)

As a complement to the specific quality conventions, these documents provide technical appendices with suggested tools to be used for each criterion. Hence, in
order to maintain the alignment between the capabilities of the SQAaaS platform and these 2 sets of guidelines, the **support for a new tool shall imply the addition
of such tool into those technical appendices**.

## How to request the support of a new tool
1) Open an issue (enhancement type) to include the tool in the guidelines.
   - Relevant links:
     - [Software-related criteria](https://github.com/indigo-dc/sqa-baseline/issues/new?assignees=orviz&labels=enhancement&template=enhancement-request.md&title=%5BENHANCEMENT%5D)
     - [Service-related criteria](https://github.com/EOSC-synergy/service-qa-baseline/issues/new?assignees=mariojmdavid%2C+orviz&labels=enhancement&template=enhancement-request.md&title=%5BENHANCEMENT%5D)
   - The issue may be accompanied by the pull request that adds the tool to the relevant appendix.
2) Create a pull request in the present repository that adds the relevant data in the [`tooling.json`](../tooling.json) file, including:
   - The tool's metadata (within `tools` property)
   - The SQA criterion or criteria where this tool does apply (by means of the `criteria` property)

## How the support is granted
Both the SQA criteria and metadata repositories are protected so that they require a minimum set of positive reviews from the core team before being merged. The
inclusion of a tool in the guidelines will immediately validate it to be part of the tooling metadata.
