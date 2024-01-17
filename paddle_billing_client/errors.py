from apiclient import exceptions
from apiclient.error_handlers import BaseErrorHandler
from apiclient.response import Response


class VerboseErrorHandler(BaseErrorHandler):
    @staticmethod
    def get_exception(response: Response) -> exceptions.APIRequestError:
        status_code = response.get_status_code()
        exception_class = exceptions.UnexpectedError

        if 300 <= status_code < 400:
            exception_class = exceptions.RedirectionError
        elif 400 <= status_code < 500:
            exception_class = exceptions.ClientError
        elif 500 <= status_code < 600:
            exception_class = exceptions.ServerError

        return exception_class(
            message=(
                f"{status_code} Error: {response.get_status_reason()} "
                f"for url: {response.get_requested_url()}"
                f"with raw data: {response.get_raw_data()}"
            ),
            status_code=status_code,
            info=response.get_raw_data(),
        )
