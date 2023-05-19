# GPT Code Review

GPT Code Review is an automatic code review application designed to provide feedback on GitLab Merge Requests using the GPT-4 model from OpenAI.

## Overview

This application listens for webhooks from GitLab whenever a merge request is created or updated. It then uses GPT-4 to generate a review of the code changes and posts this review as a comment on the merge request.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you'll need to install the following:

- Python 3.7 or later
- Git
- Pip (Python package installer)

### Installation

1.  Clone this repository:

```
git clone https://github.com/mgennings/GPT-code-review.git
cd GPT-code-review 
```

2.  Install the required Python libraries:

`pip install -r requirements.txt`

3.  Create a `.env` file with your configuration values:

`cp .env-example .env`

4.  Update the `.env` file with your OpenAI API key, GitLab URL, and GitLab private token.

### Running the Application
-----------------------

Run the application with the following command:

`python app.py`


### Contributing
------------

We welcome contributions! Please see [CONTRIBUTING.md](https://github.com./mgennings/GPT-code-review/CONTRIBUTING.md) for details on how to contribute.

### License
-------

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/mgennings/GPT-code-review/LICENSE.md) file for details.