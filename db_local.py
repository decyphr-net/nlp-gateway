TORTOISE_ORM = {
    "connections": {"default": "mysql://root:password@localhost:3306/decyphr"},
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "application.processor.models",
                "application.support.models",
            ],
            "default_connection": "default",
        }
    },
}
