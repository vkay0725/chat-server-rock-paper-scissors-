# chat-server-rock-paper-scissors!



This  implements a simple Rock-Paper-Scissors game using a client-server architecture in python. The server handles the game logic and communication between two clients.

## Files

- server.py: Implements the server that manages the game.
- client.py: Implements the client that connects to the server to play the game.

## Requirements

- Python 3.x

## How to Run

### Server

1. Open a terminal.
2. Navigate to the directory containing server.py.
3. Run the server:

    ```sh
    python3 server.py
    ```

   The server will start and listen for connections on `127.0.0.1:65244`.

### Client

1. Open two separate terminals (one for each client).
2. Navigate to the directory containing client.py.
3. Run the client in each terminal:

    ```sh
    python3 client.py
    ```

   Each client will connect to the server at `127.0.0.1:65244`.

## How to Play

1. Each client will be prompted to enter a move: `R` for Rock, `P` for Paper, or `S` for Scissors.
2. The server will determine the winner and send the result to both clients.
3. Each client will be prompted to continue the game by entering `yes` or to quit by entering `quit`.
4. If both clients choose to continue, the game will proceed with the next round. If either client chooses to quit, the game will end.

## Example

### Server Output

```
Server listening on 127.0.0.1:65244
Connected to ('127.0.0.1', 12345)
Connected to ('127.0.0.1', 12346)
```

### Client Output

```
connected to server at 127.0.0.1:65244
Enter move(R/P/S): R
received from server: You won
wish to continue?(yes/quit): yes
received from server: game continue
```

## Notes

- Ensure that the server is running before starting the clients.
- The server can handle exactly two clients at a time.
- The game will end if either client chooses to quit.
