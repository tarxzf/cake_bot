from environs import Env

env = Env()
env.read_env()

# Телеграм токен бота
token = env.str('BOT_TOKEN')

# Телеграм айди администратора бота (данный пользователь не будет отображаться в списке лидеров, так как он является админом)
admin_id = env.int('ADMIN_ID')

# Путь до файла логирования
LOGGING_FILE_PATH = 'app/data/logs.log'

# Путь до файла базы данных
DATABASE_PATH = 'app/data/sql.db'

# Минимальный множитель торта
MIN_CAKE_MULTIPLIER = 1

# Максимальный множитель торта
MAX_CAKE_MULTIPLIER = 5

# Количество торта
CAKE_AMOUNT = 100  # г

# Задержка перед съедением торта
CAKE_DELAY = 60 * 60 * 8 - 1  # 8 часов
