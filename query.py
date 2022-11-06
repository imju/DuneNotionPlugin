from dune_client.types import QueryParameter, Address, DuneRecord
from dune_client.client import DuneClient
from dune_client.query import Query

query = Query(
        name="Whale Wallets",
        query_id=1530879,
        params=[
            QueryParameter.list_type(name="Period", value=["1 hour", "4 hour", "12 hour", "24 hour"]),
            QueryParameter.number_type(name="USD amount per transaction", value=[500, 1000, 5000, 10000]),
        ],
    )

params = {"Period" : ["1 hour", "4 hour", "12 hour", "24 hour"], "USD amount per transaction" : [500, 1000, 5000, 10000]}