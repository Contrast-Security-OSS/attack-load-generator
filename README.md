# Sample Application Load Generator

These scripts can be used to generate HTTP request load for example applications. The requests contain simple examples of path traversal, SQL injection, and stored cross-site scripting (XSS) attacks. Simulated load begins at ten users and scales at increments of ten users per second until there are 100 concurrent users. After two minutes, the connections begin to close. This is repeated ten times to account for variances in system noise. Applications are not restarted between iterations, so the first iteration may vary from subsequent iterations.

## Set up

These Locust scripts require:
  - [Locust](https://github.com/locustio/locust)
	- [Spring PetClinic](https://github.com/spring-projects/spring-petclinic/tree/e2fbc561309d03d92a0958f3cf59219b1fc0d985)
	- [WebGoat 7](https://github.com/WebGoat/WebGoat/tree/2d1a89e791d6f48195039e5d8a797fd090e8b74f)

We've successfully used AdoptOpenJDK (build 11.0.10+9) with Spring PetClinic and OpenJDK (build 1.8.0_272-b10) with WebGoat 7 on Linux and Mac OS X.

Start up the app you want to test and take note of the address and port where it is listening.

## Running the load generator

Each of the scripts expects an environment variable to contain the URL for the app being tested. Edit the example below and be sure to not include any trailing slashes in the URL. Export the variable and run the script: 

### Spring PetClinic example

```
$ export PETCLINIC_URL='http://127.0.0.1:8080'
$ ./run_load_petclinic.sh
```

### WebGoat example

```
$ export WEBGOAT_URL='http://127.0.0.1:8080'
$ ./run_load_webgoat.sh
```

The load generator does not control the apps being tested, so remember to stop the apps when you're done or if you want to make any configuration changes.
