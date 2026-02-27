# Configuration settings for Bible Search

# Development configuration
DEVELOPMENT = {
    'DEBUG': True,
    'DATABASE_URI': 'sqlite:///development.db',
    'LOGGING_LEVEL': 'DEBUG'
}

# Production configuration
PRODUCTION = {
    'DEBUG': False,
    'DATABASE_URI': 'mysql://user:password@prod-db-server/bible_search',
    'LOGGING_LEVEL': 'ERROR'
}