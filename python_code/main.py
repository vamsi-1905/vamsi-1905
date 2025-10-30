
from model import Connect4Model
from agent import PlayerAgent, AIAgent
from game import play_game

def main():
    model = Connect4Model()

    # Create agents
    ai_agent = AIAgent("ai", model, depth=5)   # depth adjustable for difficulty
    model.schedule.add(ai_agent)

    # Start game
    play_game(model, ai_agent)

if __name__ == "__main__":
    main()
