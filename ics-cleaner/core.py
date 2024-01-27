import sys
import os
from pathlib import Path

# Constants
TOKEN_VALARM_START = "BEGIN:VALARM"
TOKEN_VALARM_STOP = "END:VALARM"


# Entry
paths = sys.argv[1:];

for arg in paths:
  path = Path(arg);
  
  if not (path.is_file() and path.suffix == ".ics"):
    print("Skipping. Argument is not an .ics file. Arg:" + arg)
    continue;
  
  print("Stripping...", path);
  with open(path,"r") as file:
    lines = file.readlines();
  
  isInValarmBlock = False;
  vAlarmBlocksCount = 0;
  with open(path, "w") as file:
    for line in lines:
      # Are we at the start of a valarm block?
      if line.startswith(TOKEN_VALARM_START):
        assert not isInValarmBlock, "Entering a block when already in a block! Pos:" + file.tell();
        isInValarmBlock = True;
        vAlarmBlocksCount += 1;
      
      # If we're not in a block remove the line
      if not isInValarmBlock:
        file.write(line);

      # Was this line the end of the block?
      if line.startswith(TOKEN_VALARM_STOP):
        assert isInValarmBlock, "Exiting a block when not in a block! Pos:" + file.tell();
        isInValarmBlock = False;
  
  assert not isInValarmBlock, "Reached EOF before exiting block!"
  print("Stripping COMPLETE. VALARMs removed:" + str(vAlarmBlocksCount));

print("All COMPLETE");
