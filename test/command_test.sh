#!/usr/bin/env bash

set -u

CMD=renderj2/renderj2.py
LOG=test.log
errcount=0
successcount=0
TEELOG="tee -a ${LOG}"

main() {
  loginit

  tmpfile=test/testtemplate.j2
  varfile=test/testvars.yml
  varfile2=test/testvars2.yml
  failcmdexec "${CMD} ${tmpfile}"
  failcmdexec "${CMD} nofile"
  cmdexec "${CMD} --help"
  cmdexec "${CMD} --varsfile ${varfile} ${tmpfile}"
  failcmdexec "${CMD} --varsfile nofile ${tmpfile}"
  cmdexec "${CMD} --varsfile ${varfile} --varsfile ${varfile2} ${tmpfile}"
  failcmdexec "${CMD} --varsfile ${varfile} --varsfile nofile ${tmpfile}"

  echo "success   : ${successcount}"
  echo "error     : ${errcount}"
  if [ ${errcount} -ne 0 ]; then
    exit 1
  fi
}

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

failcmdexec() {
  CMDSTR=$1

  echo -n "[${CMDSTR}]....." | ${TEELOG}

  ${CMDSTR} >> ${LOG} 2>&1
  if [ $? -eq 0 ]; then
    echo "error" | ${TEELOG}
    let errcount++
  else
    echo "ok" | ${TEELOG}
    let successcount++
  fi
  echo "" | ${TEELOG}
}

main
