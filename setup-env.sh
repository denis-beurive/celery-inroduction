# Under "bash", run:
#
#     source ./setup-env.sh

export REDIS_IP=172.16.177.128
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
__DIR__="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
PACKAGE_DIR="${__DIR__}/src"

# Set PYTHONPATH
[[ ":${PYTHONPATH}:" != *":${__DIR__}:"* ]] && export PYTHONPATH="${PACKAGE_DIR}:${PATH}"

echo "PYTHONPATH=${PYTHONPATH}"
