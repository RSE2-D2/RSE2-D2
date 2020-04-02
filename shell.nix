{
  pkgs ? import <nixpkgs> {},
  pythonPkgs ? pkgs.python37Packages
}:

with pkgs; with pythonPkgs;

mkShell {
  buildInputs = [
    python3
    tweepy
    pytest
  ];
}
