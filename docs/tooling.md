# Tooling metadata
The [tooling.json](../tooling.json) metadata file contains:
1) the [`tools`](#tool-properties) property, where the tools are described, and
2) the [`criteria`](#criteria-properties), having the mapping between the SQAaaS criteria<a href="#note1" id="note1ref"><sup>1</sup></a> and the tools.

## Tool properties
Tools are categorized under the (programming) language they apply to, so e.g. the [bandit](https://bandit.readthedocs.io/) Python tool shall be added under the `python` key:
```yaml
"tools": {
    "python": {
        "bandit": {
            "docs": "https://bandit.readthedocs.io/",
            "docker": {
                "image": "secfigo/bandit",
                "reviewed": "1970-01-01"
            }
        }
    }
}
```

The following table summarizes the properties that ought to be set in the tool definition:

| Tool property | Type | Description | Required |
| ------------- | ---- | ----------- | -------- |
| `docs` | string (url) | URL to the tool's official documentation | :heavy_check_mark: |
| `docker` | object | See [Docker](#docker-docker-property) section | :heavy_check_mark: |
| `args` | object | See [Arguments](#arguments-args-property) section | |

### Docker (`docker` property)
The `docker` property includes the information related to the availability of the Docker image that contains the tool. Hence, it offers two main ways of getting the Docker image, either 1) pulling an existing image from a Docker registry, or 2) build the image from a Dockerfile. One of the two properties must be defined:

| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `image`| string (url) | Docker registry URL (defaults to Docker Hub) | :heavy_check_mark: (only if `dockerfile` is not defined |
| `dockerfile`| string (path) | Relative path to the Dockerfile. This file shall be maintained in the present repository, under the criterion folder it applies to | :heavy_check_mark: (only if `image` is not defined |
| `reviewed`| string (date) | Date the image was last used (format YYYY-MM-DD)| |

### Arguments (`args` property)
The `args` property enables the definition of the arguments involved in the tool execution. The type of argument can fall into the three categories set out below:
- *subcommand*: many tools break up their functionality into subcommands. One popular example is the `git` tool that provides multiple subcommands (e.g. `git add`, `git commit`, ..).
- *positional*: those arguments that are required and that are defined only by their value. They can be used both with a command or a subcommand. Continuing with the example above, the `git add` subcommand always require a positional argument (e.g. `git add file1`).
- *optional*: those arguments that might be provided, but they are not required. The option name, which contains a single dash for the short version and two dashes for the long version, can be used both in conjunction with a value or, otherwise, by itself. An example is `git add --verbose file1`.

| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `type` | string (enum) | Type of the argument. Choose between [`subcommand`, `positional`, `optional`] | :heavy_check_mark: |
| `description` | string | Short description of what the tool does | :heavy_check_mark: |
| `value` | string | Argument value. When using optional arguments, the value includes both the option name and, if necessary, the associated value | |
| `args` | object | Suitable when defining commands with more than one type of argument, it allows to define nested `args` properties | |
| `selectable` | boolean | (for API clients) Whether the argument shall be customized by the user, or otherwise it is a fixed (non-modifiable) argument | |
| `format` | string (enum) | (for API clients) the value's data type. Useful for graphical interfaces, provides the means to render the form elements (inputs, text areas, dropdowns, ..). Choose between [`string`, `array`] | |

## Criteria properties



<a id="note1" href="#note1ref"><sup>1</sup></a><sub>Online versions: [software](https://indigo-dc.github.io/sqa-baseline/) and [service's](https://eosc-synergy.github.io/service-qa-baseline/) SQA criteria.</sub>