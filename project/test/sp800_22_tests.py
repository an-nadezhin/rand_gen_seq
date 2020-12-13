# X 3.1  Frequency (Monobits) Test
# X 3.2  Frequency Test within a Block
# X 3.3  Runs Test
# X 3.4  Test for the Longest Run of Ones in a Block
# X 3.5  Binary Matrix Rank Test
# X 3.6  Discrete Fourier Transform (Specral) Test
# X 3.7  Non-Overlapping Template Matching Test
# X 3.8  Overlapping Template Matching Test
# X 3.9  Maurers Universal Statistical Test
# X 3.10 Linear Complexity Test
# X 3.11 Serial Test
# X 3.12 Approximate Entropy Test
# X 3.13 Cumulative Sums Test
# X 3.14 Random Excursions Test
# X 3.15 Random Excursions Variant Test 

testlist = [
        'monobit_test',
        'frequency_within_block_test',
        'runs_test',
        'longest_run_ones_in_a_block_test',
        'binary_matrix_rank_test',
        'dft_test',
        'non_overlapping_template_matching_test',
        'overlapping_template_matching_test',
        'maurers_universal_test',
        'linear_complexity_test',
        'serial_test',
        'approximate_entropy_test',
        'cumulative_sums_test',
        'random_excursion_test',
        'random_excursion_variant_test']

print("Tests of Distinguishability from Random")

def run_tests(bits):
    results = list()

    for testname in testlist:
        print("TEST: %s" % testname)
        m = __import__("sp800_22_"+testname)
        func = getattr(m, testname)

        (success, p, plist) = func(bits)

        summary_name = testname
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            for pval in plist:
                print("P=" + str(pval))
            summary_p = str(min(plist))

        results.append((summary_name, summary_p, summary_result))

    print()
    print("SUMMARY")
    print("-------")

    for result in results:
        summary_name, summary_p, summary_result = result
        print(summary_name.ljust(40), summary_p.ljust(18), summary_result)

