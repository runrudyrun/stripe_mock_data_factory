# Stripe Mock Data Factory

This project is designed to generate test data in Stripe using fake data. It creates customers, products, prices, payment methods, and subscriptions in your Stripe test environment.

## Setup and Configuration

1. Clone the repository:
\```
git clone https://github.com/runrudyrun/stripe_mock_data_factory.git
\```

2. Install dependencies:
\```
pip install -r requirements.txt
\```

3. Set up your Stripe API key as an environment variable:
\```
export STRIPE_API_KEY=your_test_api_key
\```

## Usage

To generate the test data, run the main script:

\```
python init_stripe_project.py
\```

## TODO

1. Add more customization options for the data generation process, such as specifying the number of customers, products, and subscriptions to create.
2. Implement error handling and logging to better diagnose issues during the data generation process.
3. Add support for generating additional Stripe objects like invoices and events.
4. Create a command-line interface to easily configure the data generation process without modifying the code.
5. Add unit tests to ensure the integrity of the project and to validate the generated data.

## Contributing

Please feel free to submit issues or pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License.