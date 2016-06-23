import vlermv

v = vlermv.Vlermv('.', serializer=vlermv.serializers.identity_str,
                  key_transformer=vlermv.transformers.tuple)
print(v[('recommend', '000000001c')])
