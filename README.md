# Forecaster

Simple weather forecast service using Serverless and AWS.

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

The API and client portions are described sepately

### API

1. Install serverless
  - `$ npm install serverless -g`
2. Configure AWS CLI
  - `$ aws configure`
  - you'll need the `aws_access_key_id` and `aws_secret_access_key` for your IAM user.
3. Configure serverless
  - `$ sls config`

> Note: if you have multiple IAM users specified in `~/.aws/credentials`, you can specify which to use with serverless:
> `$ sls [config|deploy] --aws-profile <profile name>`

### Client

TBD

## Deploy

### API

Create `.secrets.yml` and add the following:
- `wunderground_api_key: <your api key>`
- `.example-secrets.yml` is provided for reference

> Do not check `.secrets.yml` into version control

Deploy the serverless framework to AWS
- `$ sls deploy`

### Client

TBD

## Testing

To manually confirm the API has successfully deployed to AWS:
```
$ sls info
#=> Service Information
#=> service: forecaster-api
#=> stage: dev
  ...
#=> endpoints:
#=>   GET - https://<api gateway address>.<region>.amazonaws.com/dev/ping

$ curl https://<api gateway address>.<region>.amazonaws.com/dev/ping
#=> "pong"
```
