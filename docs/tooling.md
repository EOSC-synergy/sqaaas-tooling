# Tooling metadata
The [tooling.json](tooling.json) metadata file contains:
1) the [`tools`](#tool-properties) property, where the tools are described, and
2) the [`criteria`](#criteria-properties), having the mapping between the SQAaaS criteria<a href="#note1" id="note1ref"><sup>1</sup></a> and the tools.

## Tool properties
Tools are categorized under the (programming) language they apply to, so e.g. a new Python tool shall be added under `tools:python:<tool>`. The following table summarizes the properties that ought to be set in the tool definition:

| Tool property | Description | Required |
| ------------- | ----------- | -------- |
| `docs` | URL to the tool's official documentation | :heavy_check_mark: |
| `docker` | See [Docker]() section | :heavy_check_mark: |
| `args` | See [Arguments]() section | |

### Docker

### Arguments (`args` property)
The `args` property enables the definition of the arguments involved in the tool execution. The type of argument can fall into the three categories set out below:
- *subcommand*: many tools break up their functionality into subcommands. One popular example is the `git` tool that provides multiple subcommands (e.g. `git add`, `git commit`, ..).
- *positional*: those arguments that are required and that are defined only by their value. They can be used both with a command or a subcommand. Continuing with the example above, the `git add` subcommand always require a positional argument (e.g. `git add file1`).
- *optional*: those arguments that might be provided, but they are not required. The option name, which contains a single dash for the short version and two dashes for the long version, can be used both in conjunction with a value or, otherwise, by itself. An example is `git add --verbose file1`.


## Criteria properties



<a id="note1" href="#note1ref"><sup>1</sup></a><sub>Online versions: [software](https://indigo-dc.github.io/sqa-baseline/) and [service's](https://eosc-synergy.github.io/service-qa-baseline/) SQA criteria.</sub>
