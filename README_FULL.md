# Polymarket Arbitrage Bot

## Introduction
This repository contains a fully functional bot designed for arbitrage trading on the Polymarket platform. The bot automatically identifies price discrepancies between markets and executes trades to capitalize on these differences.

## Features
- Automatic identification of arbitrage opportunities.
- Real-time price tracking of markets.
- Configurable trading parameters.
- Detailed logging of trades.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/valerasaharchuck-pixel/polymarket-arbitrage-bot.git
   cd polymarket-arbitrage-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   Modify the `config.py` file to set your API keys and desired trading parameters.

## Usage
1. **Run the bot:**
   ```bash
   python main.py
   ```
2. Monitor the console for trade executions and arbitrage opportunities.

## Configuration Parameters
- `API_KEY`: Your Polymarket API key.
- `TRADING_LIMIT`: Maximum amount to trade per market.
- `LOG_LEVEL`: Set to `DEBUG` for detailed logging or `INFO` for less verbosity.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature/bugfix:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push your branch and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries, please contact the maintainer at [maintainer@example.com].

## Acknowledgements
Thanks to all contributors and the Polymarket community for their support!