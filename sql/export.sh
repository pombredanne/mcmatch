#!/bin/sh
pg_dump -C -x -s > init.psql
pg_dump -Oxs -T public.arith_counter_feature -T public.mnemonic_counter_feature -T bitop_counter_feature -T call_counter_feature -T jmp_counter_feature > init_bare.psql

