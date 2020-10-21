grammar test;

program: date EOF;
date: DATE;
DATE: D'/'M;
fragment D: '0'[1-9] | '1'[0-9] | '2'[0-9] | '3'[012];
fragment M: '0'[1-9] | '1'[012];
