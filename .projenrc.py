from projen_jsii import PythonPackage

project = PythonPackage(
    author_email="dave.shepherd@unibuddy.com",
    author_name="Dave Shepherd",
    code_owners=['sabre'],
    deps=["../projen-modules/dist/python/projen_modules-0.0.0.tar.gz"],
    module_name="projen_python",
    name="projen-python",
    version="0.1.0",
)

project.synth()