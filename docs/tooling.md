# Tooling metadata
The [tooling.json](tooling.json) metadata file contains:
1) the tool metadata (under the `tools` property), and
2) the mapping between the SQAaaS criteria<a href="#note1" id="note1ref"><sup>1</sup></a> and the tools (under the `criteria` property)

## Tool properties
Tools are categorized under the (programming) language they apply to, so e.g. a new Python tool shall be added under `tools:python:<tool>`. The following table summarizes the properties that ought to be set in the tool definition:

| Tool property | Description | Required |
| ------------- | ----------- | -------- |
| `docs` | URL to the tool's official documentation | :heavy_check_mark: |
| `docker` | See [Docker properties]() | :heavy_check_mark: |
| `args` | See [Argument properties]() | |



<a id="note1" href="#note1ref"><sup>1</sup></a><sub>Online versions: [software](https://indigo-dc.github.io/sqa-baseline/) and [service's](https://eosc-synergy.github.io/service-qa-baseline/) SQA criteria.</sub>
