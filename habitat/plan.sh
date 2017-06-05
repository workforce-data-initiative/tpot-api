pkg_origin=gitgik
pkg_name=etp-api
pkg_version=0.1.0
pkg_maintainer="jee@brighthive.io, stanley@brighthive.io, aretha@brighthive.io"
pkg_upstream_url="https://github.com/workforce-data-initiative/etp-api.git"
pkg_exports=([port]=listening_port)
pkg_exposes=(port)
pkg_build_deps=(core/virtualenv)
pkg_deps=(core/python core/coreutils)
pkg_interpreters=(bin/python3)
pkg_licence=('MIT')

do_verify () {
  return 0
}

do_clean() {
  return 0
}

do_unpack() {
  # copy the contents of the source directory to the habitat cache path
  PROJECT_ROOT="${PLAN_CONTEXT}/.."

  mkdir -p $pkg_prefix
  build_line "Copying project data /src to $pkg_prefix/ ..."
  cp -r $PROJECT_ROOT/etp_api $pkg_prefix/
  cp -r $PROJECT_ROOT/tests $pkg_prefix/
  cp -r $PROJECT_ROOT/*.py $pkg_prefix/
  cp -r $PROJECT_ROOT/requirements.txt $pkg_prefix/
  build_line "Copying .env file with preset variables ..."
}

do_build() {
  pip install --upgrade pip
}

do_install() {
  cd $pkg_prefix
  build_line "Creating virtual environment ..."
  virtualenv venv
  source venv/bin/activate
  build_line "Installing requirements from requirements.txt ..."
  pip install -r requirements.txt
  build_line "Done installing requirements ..."
}
