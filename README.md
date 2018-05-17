# Forecaster

Simple weather forecast service using Serverless AWS and Vue.js.

## Prerequisites

- [Node](https://nodejs.org/en/) and [npm](https://www.npmjs.com/get-npm)
- AWS Account
  - [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) with programmatic access enabled and 'AdministratorAccess' permissions.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [Serverless](https://serverless.com/)
  - The backend uses the Serverless framework to manage resources in AWS
- [Python](https://www.python.org/downloads/release/python-365/) =~ 3.6
- Fetching data from the Weather Underground API requires an [API key](https://www.wunderground.com/weather/api/d/pricing.html)

> Note: this guide assumes a MacOS or Linux environment

## Setup

Clone this repo
  - `$ git clone git@github.com:smoip/forecaster.git` (ssh requires [some github setup](https://help.github.com/articles/connecting-to-github-with-ssh/))

The API and client portions are described separately.
Client functionality depends on the API, so you probably want to set that up first.

### API

#### Setup

Run the following from the `forecaster_api` directory
  - `cd ~/[parent dir]/forecaster/forecaster_api`

Install serverless
  - `$ npm install serverless -g`
Configure AWS CLI
  - `$ aws configure`
  - you'll need the `aws_access_key_id` and `aws_secret_access_key` for your IAM user.
Configure serverless
  - `$ sls config`
Install [Serverless Python Requirements](https://www.npmjs.com/package/serverless-python-requirements)
  - `sls plugin install -n serverless-python-requirements`
Create `.secrets.yml` (in the project root directory )and add the following:
  - `wunderground_api_key: [your wunderground api key]`
  - `.example-secrets.yml` is provided for reference
  - Do not check `.secrets.yml` into version control

> Note: if you get errors along the lines of `Could not find a version that satisfies the requirement [some python package]`
> Make sure you a) have [pip](https://pip.pypa.io/en/stable/installing/) and b) try running `forecaster_api/$ pip install [some python package]`
> ...this shouldn't happen, but just in case

#### Deploy

Deploy the serverless framework to AWS
  - `$ sls deploy`
  - take note of the `forecasterApiKey` value and the full URL of the `fetch_forecast` endpoint returned from this command
  - check [here](https://serverless.com/framework/docs/providers/aws/guide/deploying/) for deploy troubleshooting
Verify deployment
  - use the `ping` endpoint to verify your serverless stack has properly deployed
```
$ curl "[output of ping endpoint from deploy command]" --header "x-api-key:[value of forecasterApiKey]"
#=> pong
```

> Note: if you have multiple IAM users specified in `~/.aws/credentials`, you can specify which to use with serverless:
> `$ sls [config|deploy] --aws-profile [profile name]`

### Client

The client portion consists of a standalone Vue.js app.

#### Setup

Run the following form the `forecaster_client` directory
  - `cd ~/[parent dir]/forecaster/forecaster_client`

Install npm packages
  - `npm install`
Install vue-cli
  - `npm install -g @vue/cli
Set environment variables
  - open `forecaster_client/src/utils.js` in your text editor
  - replace the return values of the `apiKey` and `apiUrl` functions with the serverless generated values `forecasterApiKey` and the `fetch_forecast` endpoint respectively 
  - example:
```
export default {
  apiKey () {
    return "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  },

  apiUrl () {
    return "https://XXXXXXX.execute-api.[region].amazonaws.com/[stage]/fetch_forecast"
  }
}
```

#### Serve/Build

Run a local dev server (from the forecaster_client dir):
  - `$ npm run serve`
  - visit `localhost:8080` to run client

Build for deployment (from the forecaster_client dir):
  - `$ npm run build`
  - client app deployment instructions are outside the scope of this project
