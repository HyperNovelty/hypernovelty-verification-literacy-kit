import subprocess
import sys
import unittest
from pathlib import Path


class ValidateKitSmokeTest(unittest.TestCase):
    def test_validator_succeeds_against_repo_root(self):
        repo_root = Path(__file__).resolve().parents[1]
        script = repo_root / "scripts" / "validate_kit.py"

        result = subprocess.run(
            [sys.executable, str(script), str(repo_root)],
            cwd=repo_root,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        self.assertIn("PASS kit validation succeeded", result.stdout)


if __name__ == "__main__":
    unittest.main()
