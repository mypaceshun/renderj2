#!/usr/bin/env bash

set -u

CMD=pyrender/pyrender.py
LOG=test.log
errcount=0
successcount=0
TEELOG="tee -a ${LOG}"

loginit() {
  rm ${LOG}
  echo "********************">>${LOG}
  echo "run script" >> ${LOG}
  date >> ${LOG}
  echo "********************">>${LOG}
}

cmdexec() {
  CMDSTR=$1

  echo -n "[${CMDSTR}]....." | ${TEELOG}

  ${CMDSTR} >> ${LOG} 2>&1
  if [ $? -ne 0 ]; then
    echo "error" | ${TEELOG}
    let errcount++
  else
    echo "ok" | ${TEELOG}
    let successcount++
  fi
  echo "" | ${TEELOG}
}


loginit

tmpfile=testtemplate.j2
varfile=testvars.yml
varfile2=testvars22.yml
cmdexec "${CMD} ${tmpfile}"
cmdexec "${CMD} --help"
cmdexec "${CMD} --varsfile ${varfile} ${tmpfile}"
cmdexec "${CMD} --varsfile ${varfile} --varsfile ${varfile2} ${tmpfile}"

echo "success   : ${successcount}"
echo "error     : ${errcount}"
