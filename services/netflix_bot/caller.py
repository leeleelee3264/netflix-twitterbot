from domain.bot.usecase import BotUseCase
from services.netflix_bot.service import NetflixBotService

ues_case = BotUseCase(
    service=NetflixBotService()
)

ues_case.run()
