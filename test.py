# -*- coding: utf-8 -*-

from create_classifier import create_classifier

c, a = create_classifier('hsmp', 2000)

print c.classify({'word':'सब'})

