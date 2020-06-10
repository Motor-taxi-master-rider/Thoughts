
import itertools
import time

import wrapt

import logging

_LOGGER = logging.getLogger(__name__)


class _ExceptionNotExist(Exception):
    pass


def retry(catch_exceptions=(_ExceptionNotExist,), match_result=None, delays=(1, 1, 1, 1, 1)):
    """ Decorator for make functions retry allowed.

    :param catch_exceptions: tuple. Exception classes which is allowed to retry.
    :param match_result: function(result). Should return True if matched result is valid
    :param delays: tuple. Seconds delay for each round.
    """

    _validate_input(catch_exceptions, match_result)

    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        _ = instance
        for retry_attempt, delay in enumerate(itertools.chain(delays, [None]), start=1):
            try:
                result = wrapped(*args, **kwargs)
            except catch_exceptions as e:
                if delay is None:
                    _LOGGER.info('Maximum retry attempts is reached.')
                    raise
                else:
                    _LOGGER.info(
                        '{} {} raised exception {}. Will try in {} second(s), attempt: {}'.format(type(wrapped),
                                                                                                  wrapped.__name__,
                                                                                                  e,
                                                                                                  delay,
                                                                                                  retry_attempt))
            else:
                if not match_result:
                    # Return result immediately if do not have to check result
                    break
                elif match_result(result):
                    # Return result immediately is result is valid
                    break
                elif delay is None:
                    _LOGGER.info('Maximum retry attempts is reached.')
                    break
                else:
                    _LOGGER.info(
                        '{} {} returns {}. Will try in {} second(s), attempt: {}'.format(type(wrapped),
                                                                                         str(wrapped),
                                                                                         result,
                                                                                         delay,
                                                                                         retry_attempt))
            time.sleep(delay)

        return result

    return wrapper


def _validate_input(catch_exceptions, match_result):
    if catch_exceptions is (_ExceptionNotExist,) and not match_result:
        raise ValueError('One of catch_exceptions and match_result is required.')
