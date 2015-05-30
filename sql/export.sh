#!/bin/sh
pg_dump -C -x -s > init.psql
pg_dump -Oxs -T public.arith_counter_metric -T public.mnemonic_counter_metric -T bitop_counter_metric -T call_counter_metric -T jmp_counter_metric > init_bare.psql

