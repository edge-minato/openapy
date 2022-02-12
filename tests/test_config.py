import pytest

from openapy.config import Config, DestinationConfig, SourceConfig
from tests.conftest import DIR_NOT_FOUND, HERE, SAMPLE_APIS, TEMP_PROCESSOR_DIR


def test_source_config_default() -> None:
    sc = SourceConfig(SAMPLE_APIS.joinpath("custom"), ignore=[])
    files = [file.name for file in sc.get_files()]
    expect_files = ["__init__.py", "pet_api.py", "store_api.py", "user_api.py"]
    for exp in expect_files:
        assert exp in files


def test_source_config_ignore() -> None:
    ignore_files = ["__init__.py", "abc.py"]
    expect_files = ["pet_api.py", "store_api.py", "user_api.py"]

    sc = SourceConfig(SAMPLE_APIS.joinpath("custom"), ignore=ignore_files)
    files = [file.name for file in sc.get_files()]
    for exp in expect_files:
        assert exp in files
    for ignore in ignore_files:
        assert ignore not in files


def test_source_config_error() -> None:
    with pytest.raises(SystemExit) as e:
        _ = SourceConfig(DIR_NOT_FOUND, ignore=[])
        assert e.value.code == 1  # type: ignore


def test_destination_config_default() -> None:
    # when dest dir does exist
    dc = DestinationConfig(HERE)
    path = dc.get_output_file_path("function")
    assert path == HERE.joinpath("process_function.py")

    # when dest dir does not exist
    assert not TEMP_PROCESSOR_DIR.is_dir()
    dc = DestinationConfig(TEMP_PROCESSOR_DIR)
    assert TEMP_PROCESSOR_DIR.is_dir()
    path = dc.get_output_file_path("function")
    assert path == TEMP_PROCESSOR_DIR.joinpath("process_function.py")


def test_config() -> None:
    c = Config(SAMPLE_APIS.joinpath("custom"), "custom", True)
    files = c.source_config.get_files()
    assert len(files) == 4
