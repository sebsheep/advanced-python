from pydantic import BaseModel, ValidationError


#### YOUR CODE HERE


#### END OF YOUR CODE


def main() -> None:
    # uncomment tests as you go!
    test_player()
    # test_board()


##### DONT TOUCH CODE BELOW ###


def test_player() -> None:
    try:
        Player.model_validate_json(
            """{
                "name": "Ford",
                "score": 42,
                "favorite_color": "red",
                "from": "Betelgeuse"
            }"""
        )

        print("✅ Player validated correct json")
    except ValidationError as e:
        print("❌ Player didn't validate a correct json:")
        print(e.errors())

    try:
        Player.model_validate_json(
            """{ 
                "name": "Ford",
                "score": 42,
                "favorite_color": "yellow",
                "from": "Betelgeuse"
            }"""
        )
        print("❌ Player validated an incorrect json (color yellow is not allowed)")
    except ValidationError as e:
        print("✅ Player didn't validate incorrect json")

    try:
        Player.model_validate_json(
            """{                 
                "score": 42,
                "favorite_color": "red",
                "from": "Betelgeuse"
            }"""
        )
        print("❌ Player validated an incorrect json (name is missing)")
    except ValidationError as e:
        print("✅ Player didn't validate incorrect json")


def test_board() -> None:
    try:
        Board.model_validate_json(
            """{ 
                "players": [
                    {
                        "name": "Ford",
                        "score": 42,
                        "favorite_color": "red",
                        "from": "Betelgeuse"
                    }, 
                    {
                        "name": "Arthur",
                        "score": 69,
                        "favorite_color": "blue",
                        "from": "Earth"
                    }
                ],
                "games": ["tetris", "pong"]
            }"""
        )

        print("✅ Board validated correct json")
    except ValidationError as e:
        print("❌ Board didn't validate a correct json:")
        print(e.errors())

    try:
        Board.model_validate_json(
            """{ 
                "players": [
                    {
                        "name": "Ford",
                        "score": 42,
                        "favorite_color": "yellow",
                        "from": "Betelgeuse"
                    }, 
                    {
                        "name": "Arthur",
                        "score": 69,
                        "favorite_color": "blue",
                        "from": "Earth"
                    }
                ],
                "games": ["tetris", "pong"]
            }"""
        )
        print("❌ Board validated an incorrect json (a player has wrong color)")
    except ValidationError as e:
        print("✅ Board didn't validate incorrect json")

    try:
        Board.model_validate_json(
            """{ 
                "players": [
                    {
                        "name": "Ford",
                        "score": 42,
                        "favorite_color": "red",
                        "from": "Betelgeuse"
                    }, 
                    {
                        "name": "Arthur",
                        "score": 69,
                        "favorite_color": "blue",
                        "from": "Earth"
                    }
                ],
                "games": "tetris"
            }"""
        )
        print("❌ Board validated an incorrect json (games is not a list)")
    except ValidationError as e:
        print("✅ Board didn't validate incorrect json")


if __name__ == "__main__":
    main()
