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
| `image`| string (url) | Docker registry URL (defaults to Docker Hub) | :white_check_mark: (only if `dockerfile` is not defined |
| `dockerfile`| string (path) | Relative path to the Dockerfile. This file shall be maintained in the present repository, under the criterion folder it applies to | :white_check_mark: (only if `image` is not defined |
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
| `value` | *any type* | The value of the argument | |
| `option` | string | The option name (*only applicable for optional arguments*) | :white_check_mark: (for optional arguments) |
| `format` | string (enum) | (for API clients) the value's data type. Useful for graphical interfaces, provides the means to render the form elements (inputs, text areas, dropdowns, ..). Choose between [`string`, `array`] | :white_check_mark: (for API clients) |
| `selectable` | boolean | (for API clients) Whether the argument's value shall be customized by the user, or otherwise it is a fixed (non-modifiable) value | :white_check_mark: (for API clients) |
| `repeatable` | boolean | (for API clients) Whether the same argument can be used several times | :white_check_mark: (for API clients) |
| `args` | object | Suitable when defining commands with more than one type of argument, it allows to define nested `args` properties | |

### The `default` property
The `tools` property has a special key named `default`. Here you can define the tools that shall be available for all the defined criteria (in the [`criteria` property](#criteria-properties)).

## Criteria properties
The SQA criteria<a href="#note1" id="note1ref"><sup>1</sup></a> that the SQAaaS platform is compliant with are identified by codes, such as `QC.Sty` for styling conventions or `QC.Lic` for the requirements related to the availability and maintenance of a source code license. The `criteria` key maps the tools (the `tools` key defined in the previous section) with the SQA criteria:

```yaml
"criteria": {
    "QC.Sty": {
        "description": {
            "msg": "Use code style standards to guide your code writing so you let others understand it",
            "improves": "readability, reusability",
            "docs": "https://indigo-dc.github.io/sqa-baseline/#code-style-qc.sty"
        },
        "tools": {
            "dockerfile": ["hadolint"],
            "json": ["jsonlint"],
            "python": ["tox", "pycodestyle"]
        }
    },
    "QC.Lic": {
        "description": {
            "msg": "Usage of an open license to distribute your code",
            "improves": "external contributions, reusability",
            "docs": "https://indigo-dc.github.io/sqa-baseline/#licensing-qc.lic"
        },
        "tools": {
            "license": ["licensee"]
        }
    }
}
```

Each criterion has two properties: `description` and `tools`, which are defined as follows:
- The `tools` object contains one element per language being supported. The values are a list of tools from the ones defined in the `tools` property from the previous section.
  - Note that the tools marked as [default](#the-default-property) will be automatically added. There is no need to define those in the criterion data.
- The `description` object is meant to be used by the SQAaaS API clients. It provides information about the criterion that is suitable to contextualize it within the user interface.


<a id="note1" href="#note1ref"><sup>1</sup></a><sub>Online versions: [software](https://indigo-dc.github.io/sqa-baseline/) and [service's](https://eosc-synergy.github.io/service-qa-baseline/) SQA criteria.</sub>
