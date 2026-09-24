# Contributing

This project is intended to be reusable by anyone.

## Before opening a pull request

- Explain what changed and why.
- Test the smallest affected component.
- Do not commit credentials, private keys, tokens, personal photos, or local configuration.
- Keep hardware-specific assumptions documented.
- Prefer open-source dependencies when practical.
- Update documentation when behavior or wiring changes.

## Code style

Keep modules small and understandable. Prefer explicit error messages over silent failure.

## Hardware changes

Document:
- Exact board or module
- Voltage requirements
- Pin mapping
- Any level shifting
- Required external power
- Known limitations

Pull requests should not claim a feature is tested if it has only been designed.
