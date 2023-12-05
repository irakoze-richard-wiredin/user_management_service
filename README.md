# Branding Management System - Admin Portal

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Pre-requirement](#pre-requirement)
- [Installation](#installation)
- [License](#license)

## Overview

This system will streamline and enhance the management of Bralirwa branding assets across our extensive fleet.

### Client Information

- **Client Name:** [Bralirwa]
- **Client Url:** [Bralirwa Website](https://bralirwa.co.rw/)

## Features

- Vehicle inspection
- Billboard inspection

## Pre-requirement

- docker
- docker-compose

## Installation

###### Clone the repository
```
git clone https://pj.rexvirt.jp/gitbucket/git/BMS-Bralirwa/Admin-Portal.git
```

###### Navigate to the project directory
```
cd BMS-Portal
```

###### Set the environment variables
```
cp .env-dist .env
```
Make sure to make all the necessary changes in your .env file

###### Install docker container
```
docker-compose up -d --build
```

###### Run migrations and create super user
**In docker container bash**
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
