import pytest

from openapy.config import DestinationConfig, SourceConfig, get_Config
from tests.conftest import CONFIG_DIR, DST_DIR, SRC_APIS_DIR, log


def test_source_config_default() -> None:
    sc = SourceConfig(SRC_APIS_DIR, "", "_api.py")
    target_files = sc.get_files()
    core_names = [tf.core_name for tf in target_files]
    log(core_names)
    assert len(target_files) == 3
    assert "pet" in core_names
    assert "store" in core_names
    assert "user" in core_names


def test_source_config_with_prefix() -> None:
    sc = SourceConfig(SRC_APIS_DIR, "pet_", ".py")
    target_files = sc.get_files()
    core_names = [tf.core_name for tf in target_files]
    log(core_names)
    assert len(target_files) == 1
    assert "api" in core_names


def test_source_config_for_all() -> None:
    sc = SourceConfig(SRC_APIS_DIR, "", "")
    target_files = sc.get_files()
    core_names = [tf.core_name for tf in target_files]
    log(core_names)
    assert len(target_files) == 4


def test_destination_config_default() -> None:
    dc = DestinationConfig(DST_DIR, "process_", ".py")
    target_files = ["a", "b", "c"]
    for target_file in target_files:
        assert DST_DIR.joinpath("process_" + target_file + ".py") == dc.get_output_file_path(target_file)


def test_config_default() -> None:
    config_file = CONFIG_DIR.joinpath("example.yml")
    c = get_Config(config_file)
    assert c[0].name == "example_name"
    assert c[1].name == "per_file"


def test_invalid_config() -> None:
    for i in [1, 2, 3]:
        with pytest.raises(SystemExit) as e:
            invalid_config_file = CONFIG_DIR.joinpath(f"invalid_{i}.yml")
            _ = get_Config(invalid_config_file)
            assert e.value.code == 1  # type: ignore
