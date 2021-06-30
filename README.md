# sqa-composer-templates
Tools supported by the SQAaaS platform

## How a tool is dynamically loaded by the SQAaaS platform
1) The [SQAaaS API](https://github.com/eosc-synergy/sqaaas-api-server) loads the content of the tool's metadata file (`tooling.json`), which is then offered upon requests to `/criteria` path (see [API's spec](https://eosc-synergy.github.io/sqaaas-api-spec/#operation/get_criteria))
2) Any API client, such as the [SQAaaS web](https://github.com/eosc-synergy/sqaaas-web), can then use these metadata to compose CI/CD pipelines that include one or more of these tools in an automated fashion. 

Note that the SQAaaS platform's user does not need to provide any input for using these tools, as all the required input (Docker images, CLI arguments, etc.) are specified in the `tooling.json` file.

*Learn more about the [`tooling.json` structure.](docs/tooling.md)*

## How to contribute with new tools
Building upon the metadata, it is really straightforward to get new tools supported by the SQAaaS platform. However, tools are first assessed and subject for approval in order to ensure their relevance for the selected quality criterion.

*Learn more about the [`approval process.`](docs/approval_process.md)*
