from openapy.config import SourceConfig
from tests.conftest import SRC_APIS_DIR, log


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
