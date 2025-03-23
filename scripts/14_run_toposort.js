var CompactAdjacencyMatrix = require( '@stdlib/utils-compact-adjacency-matrix' );
var DepsGraph = require( './../output/acyclic_direct_deps_numeric.json' );
var Number2Routines = require( './../output/number_2_routine_mapping.json' );
var fs = require( 'fs' );

var adj = new CompactAdjacencyMatrix( 2052 ); // number of unique entries in `./output/direct_deps_number_format.json` (0 based indexing is followed)

// generate the adjacency matrix
for ( const [ node, edges ] of Object.entries( DepsGraph ) ) {
    for ( const edge of edges ) {
        adj.addEdge( parseInt( node ), edge );
    }
}

// run topological sort
var ordering = adj.toposort()[ 0 ].reverse()

// convert numbers to routine names
for ( var i = 0; i < ordering.length; i++ ) {
    ordering[ i ] = Number2Routines[ ordering[ i ] ];
}

// write the result to a file
fs.writeFileSync( './output/WORKING_ORDER.json', JSON.stringify( ordering, null, 2 ) );