"""Unofficial SEC EDGAR API wrapper."""
from ._types import JSONType
from typing import Union

from SecGovEdgarApi.EdgarApi import EdgarApi
from .termination.TerminationHandler import TerminationHandler
from sec_cik_mapper import StockMapper
from pathlib import Path

from SecGovEdgarApi._UserAgent import (
    BASE_USER_AGENT
)
from SecGovEdgarApi._constants import (
    SORTING_FILTERED,
)

class EdgarClient():
    """An :class:`EdgarClient` object."""

    def get_filling(ticker: str, sortingKey: str = SORTING_FILTERED, cik: str = "") -> JSONType:
        """
        :param ticker: TICKER to obtain the CIK to then get the submissions.
        :param cik: CIK to obtain submissions for.
        :param sortingKey: sortingKey is used for sorting the json output.
        :return: JSON response from an sec.gov API endpoint
            for the specified CIK, including everthing we
            can find about this the specified CIK that is in
            the param
        """

        if cik == "":
            if ticker != "":
                try: 
                    mapper = StockMapper()
                    cikTxtFile = mapper.raw_dataframe
                    cik = cikTxtFile[cikTxtFile['Ticker'] == ticker.upper()]['CIK'].values[0]
                except:
                    print("No cik found")
            else:
                print("Please fill in a ticker or a cik")

        #get all the USGaap facts that we find for this company
        dataFrames = TerminationHandler.get_usGaap(cik=cik, sortingKey=sortingKey)

        return dataFrames
    
    ####
        ## Support for sec-edgar-api https://github.com/jadchaar/sec-edgar-api
    ####
    def get_submissions(cik: str, handle_pagination: bool = True) -> JSONType:
        api = EdgarApi(user_agent=BASE_USER_AGENT)

        return api.get_submissions(cik=cik, handle_pagination=handle_pagination)

    def get_company_concept(cik: str, taxonomy: str, tag: str ) -> JSONType:
        api = EdgarApi(user_agent=BASE_USER_AGENT)

        return api.get_company_concept(cik=cik, taxonomy=taxonomy, tag=tag)

    def get_company_facts(cik: str) -> JSONType:
        api = EdgarApi(user_agent=BASE_USER_AGENT)

        return api.get_company_facts(cik=cik)

    def get_frames(taxonomy: str, tag: str, unit: str, year: str, quarter: Union[int, str, None] = None, instantaneous: bool = True ) -> JSONType:
        api = EdgarApi(user_agent=BASE_USER_AGENT)

        return api.get_frames(taxonomy=taxonomy, tag=tag, unit=unit, year=year, quarter=quarter, instantaneous=instantaneous)
