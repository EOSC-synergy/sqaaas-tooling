# Tooling metadata
The [tooling.json](../tooling.json) metadata file contains:
1) the [`tools`](#tool-properties) property, where the tools are described, and
2) the [`criteria`](#criteria-properties), having the mapping between the SQAaaS criteria<a href="#note1" id="note1ref"><sup>1</sup></a> and the tools.

## Tool properties
Tools are categorized under the (programming) language they apply to, so e.g. Python's [bandit](https://bandit.readthedocs.io/) tool shall be added under the `Python` key:
```yaml
"tools": {
    "Python": {
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
*NOTE*: the name of the languages are compliant with the ones used in the [GitHub's linguist tool](https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml). The reason
lies in the fact that file extensions for any given language are obtained from `linguist` metadata.

The following table summarizes the properties that ought to be set in the tool definition:

| Tool property | Type | Description | Required |
| ------------- | ---- | ----------- | -------- |
| `docs` | string (url) | URL to the tool's official documentation | :heavy_check_mark: |
| `docker` | object | See [Docker](#docker-docker-property) section | :heavy_check_mark: |
| `executable` | string | Name of the executable. The tool's name is used by default.  <br>*This is only required when the executable to be used is different from the tool's name* | |
| `template` | string | Name of the template to use to compose the final command (not a concatenation of `args`)) | |
| `args` | object | See [Arguments](#arguments-args-property) section | |
| `reporting` | object | See [Reporting](#reporting-reporting-property) section | |

### Docker (`docker` property)
The `docker` property includes the information related to the availability of the Docker image that contains the tool. Hence, it offers two main ways of getting the Docker image, either 1) pulling an existing image from a Docker registry, or 2) build the image from a Dockerfile. One of the two properties must be defined:

| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `image`| string (url) | Docker registry URL (defaults to Docker Hub) | :white_check_mark: (only if `dockerfile` is not defined |
| `dockerfile`| string (path) | Relative path to the Dockerfile. This file shall be maintained in the present repository, under the criterion folder it applies to | :white_check_mark: (only if `image` is not defined |
| `reviewed`| string (date) | Date the image was last used (format YYYY-MM-DD)| :heavy_check_mark: |
| `oneshot`| boolean | Set this value to `False` if you don't want the SQAaaS API to handle it as a oneshot image (i.e. adding a `sleep` command, default: `True`)| |

### Arguments (`args` property)
The `args` property enables the definition of the arguments involved in the tool execution. The type of argument can fall into the three categories set out below:
- *subcommand*: many tools break up their functionality into subcommands. One popular example is the `git` tool that provides multiple subcommands (e.g. `git add`, `git commit`, ..).
- *positional*: those arguments that are required and that are defined only by their value. They can be used both with a command or a subcommand. Continuing with the example above, the `git add` subcommand always require a positional argument (e.g. `git add file1`).
- *optional*: those arguments that might be provided, but they are not required. The option name, which contains a single dash for the short version and two dashes for the long version, can be used both in conjunction with a value or, otherwise, by itself. An example is `git add --verbose file1`.

| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `type` | string (enum) | Type of the argument. Choose between [`subcommand`, `positional`, `optional`] | :heavy_check_mark: |
| `description` | string | Short description of what the tool does | :heavy_check_mark: |
| `id` | string | Identifier of the argument (used only when `template` property is defined) | :white_check_mark: |
| `value` | *any type* | The value of the argument | |
| `option` | string | The option name (*only applicable for optional arguments*). See [Special option values](#special-option-values) section for additional customization | :white_check_mark: (for optional arguments) |
| `format` | string (enum) | (for API clients) the value's data type. Useful for graphical interfaces, provides the means to render the form elements (inputs, text areas, dropdowns, ..). Choose between [`string`, `array`] | :white_check_mark: (for API clients) |
| `selectable` | boolean | (for API clients) Whether the argument's value shall be customized by the user, or otherwise it is a fixed (non-modifiable) value. Non-selectable arguments are always set | :white_check_mark: (for API clients) |
| `repeatable` | boolean | (for API clients) Whether the same argument can be used several times | :white_check_mark: (for API clients) |
| `explicit_paths` | boolean | (for API clients) Only applicable for the assessment, whether the `value` property shall be set with the explicit list of files detected in the repository  | :white_check_mark: (for API clients) |
| `args` | object | Suitable when defining commands with more than one type of argument, it allows to define nested `args` properties | |

#### Special `option` values
The name of the `option` property might tell the SQAaaS API to perform additional work. So far it is only supported to  set credentials when the `option` value contains the following substrings:
- `jenkins-credential-id`, such as in `--kubeconfig-jenkins-credential-id`.
- `jenkins-credential-variable`, such as in `--kubeconfig-jenkins-credential-variable`.

### Reporting (`reporting` property)
The `reporting` property provides the pointers to the suitable output validator that is capable of parsing the data produced by the given tool. The list of available validator plugins officially supported in the SQAaaS platform can be found in the [sqaaas-reporting-plugins](https://github.com/eosc-synergy/sqaaas-reporting-plugins) repository.

The set of sub-properties that are meaningful to the `reporting` property are the following:
| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `validator` | string | Id of the validator (the [report2sqaaas](https://github.com/eosc-synergy/sqaaas-reporting) CLI provides the possible choices) | :heavy_check_mark: |
| `threshold` | int | The threshold that sets the output as valid or invalid  | :white_check_mark: |
| `requirement_level` | string (enum) |  Sets the relevance of the tool in regards to the fulfillment of the associated criterion. Choose between [`REQUIRED`, `RECOMMENDED`, `OPTIONAL`] | :white_check_mark: |

*Note*:
 - The `validator` and `threshold` properties are passed as input arguments to the [report2sqaaas](https://github.com/EOSC-synergy/sqaaas-reporting) module, and thus, they must be **aligned/match** those from such module.
 - The `requirement_level` of the tools is `OPTIONAL` by default (if no value is provided). Both [`REQUIRED`, `RECOMMENDED`] tools are processed by the QAA module, but only the `REQUIRED` are considered to determine the fulfillment of the criterion.

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
            "Dockerfile": ["hadolint"],
            "JSON": ["jsonlint"],
            "Python": ["tox", "pycodestyle"]
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
