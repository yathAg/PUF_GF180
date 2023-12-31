# Copyright 2022 GlobalFoundries PDK Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

########################################################################################################################
## layers definition for Klayout of GF180MCU
########################################################################################################################

layer = {
    "comp": (22, 0),
    "dnwell": (12, 0),
    "nwell": (21, 0),
    "lvpwell": (204, 0),
    "dualgate": (55, 0),
    "poly2": (30, 0),
    "nplus": (32, 0),
    "pplus": (31, 0),
    "sab": (49, 0),
    "esd": (24, 0),
    "contact": (33, 0),
    "metal1": (34, 0),
    "via1": (35, 0),
    "metal2": (36, 0),
    "via2": (38, 0),
    "metal3": (42, 0),
    "via3": (40, 0),
    "metal4": (46, 0),
    "via4": (41, 0),
    "metal5": (81, 0),
    "via5": (82, 0),
    "metaltop": (53, 0),
    "pad": (37, 0),
    "resistor": (62, 0),
    "fhres": (227, 0),
    "fusetop": (75, 0),
    "fusewindow_d": (96, 1),
    "polyfuse": (220, 0),
    "mvsd": (210, 0),
    "mvpsd": (11, 39),
    "nat": (5, 0),
    "comp_dummy": (22, 4),
    "poly2_dummy": (30, 4),
    "metal1_dummy": (34, 4),
    "metal2_dummy": (36, 4),
    "metal3_dummy": (42, 4),
    "metal4_dummy": (46, 4),
    "metal5_dummy": (81, 4),
    "metaltop_dummy": (53, 4),
    "comp_label": (22, 10),
    "poly2_label": (30, 10),
    "metal1_label": (34, 10),
    "metal2_label": (36, 10),
    "metal3_label": (42, 10),
    "metal4_label": (46, 10),
    "metal5_label": (81, 10),
    "metaltop_label": (53, 10),
    "metal1_slot": (34, 3),
    "metal2_slot": (36, 3),
    "metal3_slot": (42, 3),
    "metal4_slot": (46, 3),
    "metal5_slot": (81, 3),
    "metaltop_slot": (53, 3),
    "ubmpperi": (183, 0),
    "ubmparray": (184, 0),
    "ubmeplate": (185, 0),
    "schottky_diode": (241, 0),
    "zener": (178, 0),
    "res_mk": (110, 5),
    "opc_drc": (124, 5),
    "ndmy": (111, 5),
    "pmndmy": (152, 5),
    "v5_xtor": (112, 1),
    "cap_mk": (117, 5),
    "mos_cap_mk": (166, 5),
    "ind_mk": (151, 5),
    "diode_mk": (115, 5),
    "drc_bjt": (127, 5),
    "lvs_bjt": (118, 5),
    "mim_l_mk": (117, 10),
    "latchup_mk": (137, 5),
    "guard_ring_mk": (167, 5),
    "otp_mk": (173, 5),
    "mtpmark": (122, 5),
    "neo_ee_mk": (88, 17),
    "sramcore": (108, 5),
    "lvs_rf": (100, 5),
    "lvs_drain": (100, 7),
    "ind_mk1": (151, 5),
    "hvpolyrs": (123, 5),
    "lvs_io": (119, 5),
    "probe_mk": (13, 17),
    "esd_mk": (24, 5),
    "lvs_source": (100, 8),
    "well_diode_mk": (153, 51),
    "ldmos_xtor": (226, 0),
    "plfuse": (125, 5),
    "efuse_mk": (80, 5),
    "mcell_feol_mk": (11, 17),
    "ymtp_mk": (86, 17),
    "dev_wf_mk": (128, 17),
    "metal1_blk": (34, 5),
    "metal2_blk": (36, 5),
    "metal3_blk": (42, 5),
    "metal4_blk": (46, 5),
    "metal5_blk": (81, 5),
    "metalt_blk": (53, 5),
    "pr_bndry": (0, 0),
    "mdiode": (116, 5),
    "metal1_res": (110, 11),
    "metal2_res": (110, 12),
    "metal3_res": (110, 13),
    "metal4_res": (110, 14),
    "metal5_res": (110, 15),
    "metal6_res": (110, 16),
    "border": (63, 0),
}

print(layer["comp"])
