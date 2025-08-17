from fastapi import APIRouter, HTTPException
from app.PlayBlackJack import play_blackjack

router = APIRouter(
    prefix="/play",
    tags=["Play"]
)

blackjack_game = play_blackjack.PlayBlackJack()


@router.get("/status")
async def get_status():
    return blackjack_game.get_game_status()


@router.post("/hit")
async def player_hit():
    return blackjack_game.player_hit()


@router.post("/stand")
async def player_stand():
    return blackjack_game.play_dealer()
