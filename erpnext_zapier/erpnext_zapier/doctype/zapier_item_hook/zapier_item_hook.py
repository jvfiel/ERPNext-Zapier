# -*- coding: utf-8 -*-
# Copyright (c) 2018, johnvincentfiel@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class ZapierItemHook(Document):
    pass


# bench execute erpnext_zapier.erpnext_zapier.doctype.zapier_item_hook.zapier_item_hook.test_zap
def test_zap():
    doc = frappe.get_doc("Item", "ABC")
    zap(doc)


def zap(doc,request_method="Put"):
    # doc = frappe.get_doc("Item", "ABC")
    fields = """"""

    for i,field in enumerate(frappe.get_doc("Zapier Item Hook").item_fields):
        if i > 0:
            fields += ", "
        fields += field.field_name


    # print doc.as_dict()
    import requests

    # new_dict = {}
    if request_method != "Post":
        new_dict = frappe.db.sql("""SELECT {0} FROM `tabItem` WHERE name='{1}'""".format(fields, doc.name), as_dict=True)[0]
        print new_dict
        print "############################"
        clean_dict = {}
        for key, value in enumerate(new_dict):
            if value:
                clean_dict.update({key: value})
                # print "not None and not []"
                # print key, "=", value
    elif request_method == "Post":
        doc_dict = doc.as_dict()
        clean_dict = {}
        for i, field in enumerate(frappe.get_doc("Zapier Item Hook").item_fields):
            clean_dict.update({field: doc_dict[field.field_name]})

    if frappe.db.get_value("Zapier Item Hook", None, "zapier_hook_url"):

        # print new_dict
        if request_method == "Put":
            r = requests.put(frappe.db.get_value("Zapier Item Hook", None, "zapier_hook_url"),
                              data=clean_dict)
        elif request_method == "Post":
            r = requests.post(frappe.db.get_value("Zapier Item Hook", None, "zapier_hook_url"),
                             data=clean_dict)
        elif request_method == "Delete":
            r = requests.delete(frappe.db.get_value("Zapier Item Hook", None, "zapier_hook_url"),
                             data=clean_dict)

        print r.headers
        print "###########################"
        print "###########################"
        print "###########################"
        print "###########################"
        print "###########################"
        print "###########################"
        print(r.status_code, r.reason)
        print(r.text[:300] + '...')

    else:
        frappe.publish_realtime(event='msgprint',
                                message='Zapier not setup.',
                                user=frappe.session.user)


# bench execute erpnext_zapier.erpnext_zapier.doctype.zapier_item_hook.zapier_item_hook.validate
def validate(doc, method):
    exists = frappe.db.sql("""SELECT Count(*) FROM `tabItem` WHERE name='{0}'""".format(doc.name))
    if exists[0][0] > 0:
        zap(doc, request_method="Put")

def after_insert(doc,method):
    zap(doc,request_method="Post")

def on_trash(doc,method):
    zap(doc,request_method="Delete")


def test_zap2():
    import requests

    # try:
    r = requests.post("https://hooks.zapier.com/hooks/catch/2929690/zdizho/",
                      data={"item_code":"hello world"})

    print r.headers
    print "###########################"
    print(r.status_code, r.reason)
    print(r.text[:300] + '...')
    # except:
    #     pass