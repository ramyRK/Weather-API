Weather API Project

This project is a simple RESTful API for fetching weather data built using Django and Django REST Framework (DRF). It allows users to retrieve current weather information for a specified city by integrating with a third-party weather service. The API uses Redis to cache responses and environment variables to securely manage configuration settings.

Project URL: [Weather API Project](https://roadmap.sh/projects/weather-api-wrapper-service)


Features

    Retrieve Weather Data: Get current weather information for a specified city.
    Caching: Responses are cached in Redis with an expiration time to reduce external API calls.
    Secure Configuration: Environment variables are used to manage sensitive data like API keys and connection strings.
    Error Handling: Gracefully handles errors such as missing or invalid city parameters and external API failures.
