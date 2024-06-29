from projen.python import PythonProject

project = PythonProject(
    author_email="dave.shepherd@endor.me.uk",
    author_name="Dave Shepherd",
    module_name="projen_python",
    name="projen-python",
    version="0.1.0",
)

project.synth()