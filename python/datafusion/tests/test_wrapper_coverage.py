import datafusion
import datafusion.functions
import datafusion.object_store
import datafusion.substrait


def missing_exports(internal_obj, wrapped_obj) -> None:
    for attr in dir(internal_obj):
        assert attr in dir(wrapped_obj)

        internal_attr = getattr(internal_obj, attr)
        wrapped_attr = getattr(wrapped_obj, attr)

        assert wrapped_attr is not None if internal_attr is not None else True

        if attr in ["__self__", "__class__"]:
            continue
        if isinstance(internal_attr, list):
            assert isinstance(wrapped_attr, list)
            for val in internal_attr:
                assert val in wrapped_attr
        elif hasattr(internal_attr, "__dict__"):
            missing_exports(internal_attr, wrapped_attr)


def test_datafusion_missing_exports() -> None:
    """Check for any missing pythone exports.

    This test verifies that every exposed class, attribute, and function in
    the internal (pyo3) module is also exposed in our python wrappers.
    """
    missing_exports(datafusion._internal, datafusion)
