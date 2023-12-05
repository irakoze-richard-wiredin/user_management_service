# User Management Service - Irembo

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Pre-requirement](#pre-requirement)
- [Installation](#installation)
- [License](#license)

## Overview

This system will:
- Ease the on-boarding process of new users.
- Highly available and performant application to handle 1000’s of requests simultaneously.
- Store and manage user data at orders of magnitude of scale.
- Implement best in class security features.

### Client Information

- **Client Name:** [Irembo]

## Features

- Ability to create an account - signup
- Login and Logout
- Reset password
- Update profile
- Apply for account verification

## Pre-requirement

- docker
- docker-compose

## Installation

###### Clone the repository
```
git clone https://github.com/irakoze-richard-wiredin/user_management_service.git
```

###### Navigate to the project directory
```
cd user_management_service
```

###### Set the environment variables
```
cp .env-dist .env
```
Make sure to make all the necessary changes in your .env file

###### Build the project container
```
docker-compose up -d --build
```