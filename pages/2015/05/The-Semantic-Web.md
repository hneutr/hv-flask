title: The Semantic Web
description: Originally written for 'Internet-scale Distributed Systems'
date: 2015-05-01
kind: projects
tags: [web]

---

<div class="report">
	<div class="section" id="table_of_contents">
		<h2 class="section-title">Table of Contents</h2>
		<ol>
			<li class="section-ref"><a class="section-ref-a" href="#Introduction">Introduction</a></li>
			<li class="section-ref">
				<a class="section-ref-a" href="#What_is_the_Semantic_Web">What is the Semantic Web and What Does it Do?</a>
				<ol>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Linked_Data">Linked Data</a>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Queries">Queries</a>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Ontologies">Ontologies</a>
					</li>
				</ol>
			</li>
			<li class="section-ref">
				<a class="subsection-ref" href="#Components">Components of the Semantic Web</a>
				<ol>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Representation">Knowledge Representation</a>
						<ol>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Representation-Vagueness">Representation Vagueness</a>
							</li>
						</ol>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Inference">Inference</a>
						<ol>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Inference-Inconsistency">Inference Inconsistency</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Inference-Uncertainty">Inference Uncertainty</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Inference-Vagueness">Inference Vagueness</a>
							</li>
						</ol>
					</li>
				</ol>
			</li>
			<li class="section-ref">
				<a class="subsection-ref" href="#Implementation">Implementation of the Semantic Web</a>
				<ol>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Implementation_Representations">Knowledge Representation and Ontology Implementations</a>
						<ol>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-RDFa">Resource Description Framework in Attributes (RDFa)</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-Microformats">Microformats</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-Microdata">Microdata</a>
							</li>
						</ol>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#W3C_Ontologies">W3C Ontology Implementations</a>
						<ol>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-RDFS">Resource Description Framework Schema (RDFS)</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-OWL">Web Ontology Language (OWL)</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-SKOS">Simple Knowledge Organization System (SKOS)</a>
							</li>
						</ol>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#W3C_Stack">Other Technologies in the W3C Semantic Web Stack</a>
						<ol>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-SPARQL">Simple Protocal and RDF Query Language (SPARQL)</a>
							</li>
							<li class="subsection-ref">
								<a class="subsection-ref-a" href="#Implementation-RIF">Rule Interchange Format</a>
							</li>
						</ol>
					</li>
				</ol>
			</li>
			<li class="section-ref">
				<a class="subsection-ref" href="#Issues">Issues Facing the Semantic Web</a>
				<ol>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Quantity">Quantity of Information</a>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Barriers_to_entry">Barriers to Entry</a>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Deception">Deception</a>
					</li>
					<li class="subsection-ref">
						<a class="subsection-ref-a" href="#Censorship">Censorship</a>
					</li>
				</ol>
			</li>
			<li class="section-ref"><a class="subsection-ref" href="#Progress">Progress Towards the Semantic Web</a></li>
			<li class="section-ref"><a class="subsection-ref" href="#Conclusion">Conclusion</a></li>
			<li class="section-ref"><a class="subsection-ref" href="#Bibliography">Bibliography</a></li>
		</ol>
	</div>
	<hr>
	<div class="section" id="Introduction">
		<h2 class="section-title">Introduction</h2>
		<p>The Semantic Web is an extension of the traditional Web beyond documents and applications into the realm of <em>data</em>. Tim Berners-Lee describes the Semantic Web as a system that would "open up the knowledge and workings of humankind to meaningful analysis by software agents" <a href="#scientific_american">[1]</a>. The Semantic Web differs from the Web in two key ways: there can be relations between URIs, and URIs can be used to describe objects, rather than simply documents. With these two additional tools, information on the Web could be used to make statements about objects in both the physical world and online. The Semantic Web refers to the specific case in which these statements are machine-readable, and therefore machine-explorable. In such a Web, computer-agents could answer user-queries via inference, using the links between statements to traverse the search space. Though Tim introduced the idea of the Semantic Web more than fifteen years ago, content that supports Semantic Web makes up a tiny fraction of the Web. Implementation of the Semantic Web has been slow, and there many obstacles - technical, logical, and practical - to its widespread implementation. The Web, as it is now, is not really a Semantic Web - though a number of sites do support Semantic content - but it could become one.</p>

		<p> The advent of the Web changed the way documents were shared. It leveraged existing technologies, and by integrating those technologies it provided a common ground for sharing information. There are many reasons the Web succeeded, but one of the most significant - and deeply consequential to the implementation of a Semantic Web - was that it was designed for human agents. This is apparent in the Web's methods of content transmission (HTTP/1.0 headers were text/plain <a href="#rfc_1945_3.5">[2]</a>; URIs are plaintext <a href="#rfc_1945_3.4">[3]</a> and, though they are not required to, "are primarily intended for human interpretation" <a href="#rfc_3986">[4]</a>) and in its content itself (HTML is declarative and self-describing). Lowering the barriers to entry makes adopting a technology easier, encouraging network effects. The emphasis on human-readability in Tim's original Web played a key role in the success of the internet.</p>

		<p>In 1991, when Tim announced the first version of his World Wide Web, the idea of a global, distributed, and human-explorable information network was novel and revolutionary <a href="#www_announcement">[5]</a>. Though it might have been possible, the merit of adding further features to the Web to make it machine-explorable would have appeared questionable at best; there wasn't yet enough information online to make that type of exploration attractive, and even if there had been, the kinds of programs that might explore in this way didn't exist yet. As the amount of information on the Web grew, services rooted in machine-exploration of the Web, like Search, began to flourish.</p>

		<p>These tools took advantage of the self-describing nature of HTML to extract meaning from webpages, examining only the "raw textual content... in the HTTP response body" <a href="#understanding_web_pages_better">[6]</a>. With the introduction of JavaScript in 1995, the variety of data the Web could support increased dramatically <a href="#javascript_announcement">[7]</a>. Though JavaScript made it possible to create robust Web applications, it simultenously made machine-interpretation of Web content more difficult and the value of such exploration more valuable. JavaScript lets you do more, this power comes at the cost of transparency. The goal of the Semantic Web is to make data on the modern Web, in spite of its profusion of technologies, clear and accessible.</p> 

		<p> The value in the Semantic Web lies in its ability to reduce vast quantities of data on the Web in a way that is meaningful to a user. As the amount of data on the Web increases <a href="#2014_bots">[8]</a>, as we spend more time on the Web (7.5 hours per day, 186% more in 2014 than 2010 <a href="#statistica_internet_time">[9]</a>), and as that data is more meaningfully integrated into our lives <a href="#wired_iot">[10]</a>, the value a World Wide Semantic Web would provide increases.</p>
	</div>
	<hr>
	<div class="section" id="What_is_the_Semantic_Web">
		<h2 class="section-title">What is the Semantic Web and What Does it Do?</h2>
		<p>The Semantic Web refers to the idea of an extension to the World Wide Web in which there are standardized methods for sharing data.
		that would provide common methods for sharing data. The endgoal of the Semantic Web is to "enable computers to do more useful work" via enabling machine-exploration of 'Linked Data' across the web <a href="#w3c_semantic_overview">[11]</a>. There can be no Semantic Web without Linked Data, and as such the standardization of Linked Data is the primary objective for proponents of the Semantic Web.</p>

		<div class="subsection" id="Linked_Data">
			<h3 class="subsection-title">Linked Data</h3>
			<p>Tim specifies four qualities necessary for data to be considered linked:</p>    
			<ol>
				<li><p>"Use URIs as names for things.</p></li>
				<li><p>Use HTTP URIs so that people can look up those names.</p></li>
				<li><p>When someone looks up a URI, provide useful information using the standards</p></li>
				<li><p>Include links to other URIs. so that they can discover more things." <a href="#tim_linked_data">[12]</a></p></li>
			</ol>
			<p>This definition of Linked Data specifies the conditions necessary for Semantic Web-supporting data. The first condition guarantees names on the Semantic Web, just as on the Web, dereference uniquely, regardless of whether or not they indicate a resource. However, it also expands the types of things URIs can represent beyond Web documents; on the Semantic Web, a URI can refer to any kind of information, whether it be a person, a document, an application, or a value. The second condition applies to content on the Web and on the Semantic Web equally, and ensures the Semantic Web is compatible with the World Wide Web.</p>

			<p>The final two conditions for Linked Data are what differentiate the Semantic Web from the Web. A Semantic Web URI dereference must <em>by default</em> provide the dereferencer with both <em>standardized</em> information about the dereferenced URI (condition three) and a set of URIs <em>related</em> to the dereferenced URI (condition four). A dereference on the Semantic Web does not necessarily link to a document; instead, it provides information about that URI and how it is connected to other content on the Semantic Web. These characteristics make Linked Data self-describing.</p>
		</div>
		<div class="subsection" id="Queries">
			<h3 class="subsection-title">Queries</h3>
			<p>Linked Data is not a goal in and of itself; rather, it is a prerequisite for query-resolution by machines, the core feature of the Semantic Web. Query-resolution upon Linked Data is significantly different from Query-resolution in traditional relational databases: over Linked Data, a result is obtained by recursively exploring connections in an instance of Linked Data to other distributed instances of Linked Data; over relational databases, queries are assessed by accessing tables within that database. Relational databases are 'flat' and can be thought of linearly; Linked Data forms a graph <a href="#semantic_queries_in_databases">[13]</a>.

			<p>Query-resolution over Linked Data has a number of advantages over Relational Database query-resolution, particularly in a decentralized and distributed environment like the Web. First, querying data spread across multiple sources is handled easily by the graph-structure of Linked Data, as opposed to requiring joining different relational databases. Second, because it Linked Data query-resolution occurs over HTTP, caching can be implemented easily <a href="#advantages_of_RDF">[14]</a>.</p>
		</div>
		<div class="subsection" id="Ontologies">
			<h3 class="subsection-title">Ontologies</h3>
			<p>The set of rules that define the validity of a statement and the logic of the inference rules for some Linked Data is called an Ontology or a Vocabulary <a href="#w3c_vocabularies">[15]</a>. Multiple Vocabularies can exist on the Semantic Web, though the value of a Vocabulary is closely related to the amount of information within it. Per Metcalfe's Law, a single large Vocabulary provides more value than two Vocabularies half the size <a href="#metcalfes_law_semantic">[16]</a>.</p>

			<p>An Ontology must be internally consistent to be useful, but there is no requirement that different ontologies be consistent between each other. This issue is discuess further in the <a href="#W3C_Ontologies">Implementation Ontologies</a> section.</p>
		</div>
	</div>
	<hr>
	<div class="section" id="Components">
		<h2 class="section-title">Components of the Semantic Web</h2>
		<p>There are two components to an Ontology: Knowledge Representation, and Inference Rules. In coordination with Linked Data, these two components make machine-resolution of queries possible.</p>

		<div class="subsection" id="Representation">
			<h3 class="subsection-title">Knowledge Representation</h3>
			<p>The Semantic Web differs from the Web by attaching meaning to content. The meaning of this content is used to facilitate  machine-exploration and query-resolution. A Knowledge Representation system sets out a method to associate attributes with objects. Given the distributed nature of the Semantic Web, several special considerations must be taken in structuring a knowledge representation system.</p>

			<ul>
				<li>
					<h4 class="subsection-subtitle" id="Representation-Vagueness"> Vagueness </h4>
					<p>Vague statements pose an interesting challenge for any knowledge representation system, and the way these statements are handled has a deep effect on what that system can be used for. A statement is vague when "there are possible states of things concerning which it is <em>intrinsically uncertain</em> whether [those states are] excluded or allowed by the proposition... because the speaker's habits of language were indeterminate" <a href="#stanford_vagueness">[17]</a>. The sentence "Hunter is young" is a vague sentence, as the meaning of 'young' is contenxt dependent.</p>
				</li>
			</ul>

			<p>Knowledge Representation systems that are able to describe an unbounded number of subjects, objects, and relations are realistically guaranteed to contain vague statements. On the other hand, a bounded Knowledge Representation system might avoid the issue of vague statements by sufficiently restricting the set of allowable statements.</p>
		</div>
		<div class="subsection" id="Inference">
			<h3 class="subsection-title">Inference</h3>
			<p>Inference is the last component of the Semantic Web necessary for automatic Query-resolution. In the Semantic Web, inference is the process by which "automatic procedures can generate new relationships based on the data and based on some additional information in the form of a vocabulary" <a href="#w3c_inference">[18]</a>. There are three issues related to Inference which require special attention:</p>
			<ul>
				<li>
					<h4 class="subsection-subtitle" id="Inference-Inconsistency">Inconsistency</h4>
					<p>Any Inference rule for use on the Semantic Web must deal with inconsistencies. This is a deep and fundamental logical issue, as in Aristotelian Logic, a contradiction entails <em>anything</em>, a result that is unacceptable on the Semantic Web <a href="#logical_inconsistency">[19]</a>. A logical system is described as 'explosive' if, in that system, "<em>A</em> and <em>not A</em> entails <em>B</em>, for every <em>A</em> and <em>B</em>" <a href="#logical_paraconsistency">[20]</a>. Deafeasible Reasoning Systems, like paraconsistent logic, are non-explosive, promoting a weaker for of logic in which contradictions are permissible <a href="#defeasible_logic">[21]</a>. These kinds of non-explosive inference systems are generally used on the Semantic Web.</p>
				</li>
				<li>
					<h4 class="subsection-subtitle" id="Inference-Uncertainty">Uncertainty</h4>
					<p>Regardless of the Knowledge Representation System, there are some queries for which there is more than one possible answer. As an example, if the data is 'a polygon with four sides of equal length meeting at right angles' and the query is 'what shape is this polygon?', there are two equally valid answers, though they differ in specificity: 'square' or 'rectangle'. Probabilistic analysis can be used to determine the most likely answer in these situations <a href="#calculating_uncertainty">[22]</a>.</p>
				</li>
				<li>
					<h4 class="subsection-subtitle" id="Inference-Vagueness">Vagueness</h4>
					<p>If vague statements are allowed in the Knowledge Representation system, the inference rules must have some means of assessing their truth-value in order. Fuzzy Logic, where truth statements are assigned a decimal value between 0 and 1 (as opposed to a binary one in traditional logic), can be applied in this situation <a href="#fuzzy_logic">[23]</a>.</p>
				</li>
			</ul>
		</div>
	</div>
	<hr>
	<div class="section" id="Implementation">
		<h2 class="section-title">Implementation of the Semantic Web</h2>
		<p>There are a number of implementations of Semantic Web technologies, and each implementation is administered by a different group. Each of these systems makes different design decisions which impact their ease of use, expressiveness, and extensibility. Many of the Semantic Web technologies implemented feature a tight coupling between Inference Rules, Knowledge Representation, Ontology, and Query Language.</p>
		<div class="subsection" id="Implementation_Representations">
			<h3 class="subsection-title">Knowledge Representation Implementations</h3>
			<ul>
				<li id="Implementation-RDFa">
					<h4 class="subsection-subtitle">RDFa (Resource Description Framework in Attributes)</h4>
					<p>The W3C proposes RDFa as the standard format for Semantic Web knowledge representation, with the aim of solving "the problem of marking up machine-readable data in HTML documents" <a href="#w3c_rdfa">[24]</a>. RDFa uses subject-predicate-object triples, is capable of describing arbitrary relations and IRIs <a href="#w3c_rdfa_triples">[25]</a>. The subject identifies what the statement is about; the predicate identifies the type of relation in the statement; and the object indicates the value that the subject takes for the predicate. The W3C spec specifies that subjects and predicates must be IRIs, but objects may be literals. This requirement stipulates that subjects and predicates be unique references, while the object can have any value.</p>
				</li>
				<li id="Implementation-Microformats">
					<h4 class="subsection-subtitle">Microformats</h4>
					<p>Microformats are an alternative to RDFa. The key difference between microformats and RDFa is that microformats, unlike RDFa, are not "Infinitely extensible and open-ended" <a href="#microformats">[26]</a>. Microformats are meant to reuse existing data formats, like hCard, for Semantic Web markup and have a low barrier to entry.</p>
				</li>
				<li id="Implementation-Microdata">
					<h4 class="subsection-subtitle">Microdata</h4>
					<p>Microdata is another alternative, and supported by many of the major Search engines <a href="#microdata">[27]</a>. This format defines relations on the <a href="schema.org">schema.org</a> website. Like microformats, the microdata format does not allow arbitrary attributes to be defined. However, unlike microformats, which aims to reuse existing formats, the creators of microdata define their own attributes and relations.</p>
				</li>
			</ul>
			<p>A more complete overview on the differences between RDFa, Microdata, and Microformats can be found <a href="http://manu.sporny.org/2011/uber-comparison-rdfa-md-uf/">here</a>.</p>
		</div>
		<div class="subsection" id="W3C_Ontologies">
			<h3 class="subsection-title">W3C Ontology Implementations</h3>
			<p>The W3C has developed a number of ontologies, each for a different purpose.</p>
			<ul>
				<li id="Implementation-RDFS">
					<h4 class="subsection-subtitle">RDFS (Resource Description Framework Schema)</h4>
					<p>RDFS is an ontology that extends the RDF Knowledge Representation Format, providing a "mechanisms for describing groups of related resources and the relationships between these resources." <a href="#w3c_rfds">[28]</a></p>
				</li>
				<li id="Implementation-OWL">
					<h4 class="subsection-subtitle">OWL (Web Ontology Language)</h4>
					<p>OWL, unlike RDF, RDFa, or RDFS, which define abstract ways objects can relate, is an ontology with a "formally defined meaning" <a href="#w3c_owl_2">[29]</a>. This ontology is specifically intended to be used for information that "needs to be processessed, as opposed to situations where the content only needs to be presented to humans" <a href="#w3c_owl">[30]</a>.</p>
				</li>
				<li id="Implementation-SKOS">
					<h4 class="subsection-subtitle">SKOS (Simple Knowledge Organization System)</h4>
					<p>SKOS is an ontology which "aims to provide a bridge between different communities of practice within the library and information sciences involved in the design and application of knowledge organization systems" <a href="#w3c_skos">[31]</a>.</p>
				</li>
			</ul>
		</div>
		<div class="subsection" id="W3C_Stack">
			<h3 class="subsection-title">Other Technologies in the W3C Semantic Web Stack</h3>
			<p>There are a number of other tools in the W3C Semantic Web Stack.</p>

			<ul>
				<li id="Implementation-SPARQL">
					<h4 class="subsection-subtitle">SPARQL (Simple Protocal and RDF Query Language)</h4>
					<p>SPARQL is the W3C standard Semantic Query Language. SPARQL supports "aggregation, subqueries, negation, creating value expressions, extensible value testing, and constraining queries by source RDF graph" <a href="#w3c_sparql">[32]</a>.</p>
				</li>
				<li id="Implementation-RIF">
					<h4 class="subsection-subtitle">RIF (Rule Interchance Format</h4>
					<p>RIF is a W3C initiative which "aims to develop a standard for exchanging rules among disparate systems, especially on the Semantic Web" <a href="#rif">[33]</a>. The initiative aims to develop a group of interoperable languages, using those language's rigorously defined semantics and syntax to accomplish this task.
					</p>
				</li>
			</ul>
		</div>
	</div>
	<hr>
	<div class="section" id="Issues">
		<h2 class="section-title">Isues Facing the Semantic Web</h2>
		<p>There are many obstacles to the realization of the Semantic Web, the most substantial of which are: the sheer quantity of information to be described; intentionally fraudulent or false data; high barriers to Semantic Web content creation; and the possible misuse of Semantic Resources.</p>
		<div class="subsection" id="Quantity">
			<h3 class="subsection-title">Quantity</h3>
			<p>The massive volumne of pages and data on the Web is the single greatest challenge to the spread of the Semantic Web. There are 4.54 billion pages as of May 2015, and marking up each of those pages with Semantic Web metadata is far from trivial <a href="#number_of_webpages">[34]</a>. That said, the size of the Web is a double-edged sword, increasing the value of a widespread Semantic Web.</p>
		</div>
		<div class="subsection" id="Barriers_to_entry">
			<h3 class="subsection-title">Barriers to Entry</h3>
			<p>The high learning curve of most Semantic Web technologies makes widespread adoption difficult. Compare the learning curve of HTML to the Semantic Web: to learn basic HTML, a user need only learn a few dozen tags; to learn 'basic' Semantic Markup, the user must have knowledge of how statements are written in the Knowledge Representation format, be familiar with the ontology they are working with <em>right now</em>.</p>

			<p>Complaints about the high barriers to entry are levied against the W3C Semantic Web Stack in particular, and one of the reasons some choose to markup their pages with the simpler Microdata or Microformat Knowledge Representation formats. Ultimately, the decision to implement Semantic Content is a value judgement of the user. Given the endgoal of a global web of data, the ease with which content can be added to the Semantic Web is serious point.</p>

			<p>Implementing Semantic Web markup does place a burden on the user, but this is a tradeoff for the gain in value that markup information provides. There's no free lunch - in order to get more out of a system, you have to put more in. The trick is to strike the right balance between expressiveness and ease of implementation.</p>
		</div>
		<div class="subsection" id="Deception">
			<h3 class="subsection-title">Deception</h3>
			<p>Intentionally incorrect or misleading data poses a significant problem for the Semantic Web. The Semantic Web's key offering - increased convenience and access to data via automatic machine-exploration - is dependent on total user trust. As a result, the Semantic Web's margin for error when it comes to deceit is quite small, as even a small mistake can undermine the user's confidence in the System. Cryptographic techniques can be used to address the issue of authorship of a Semantic Web statement.</p>
		</div>
		<div class="subsection" id="Censorship">
			<h3 class="subsection-title">Censorship</h3>
			<p>The Semantic Web would make machine-understanding easier and more widespread, and it is possible this could be used to more aggressively censor content. I think this is one of the strongest points against the Semantic Web, as it presents a real potential negative effect of implementing such a global system. However, many of the arguments that advocate against its implementation could be made against the Web itself. Many powerful systems that provide real and significant value also open up new avenues for malicious actions; any tool can be used for good or bad. That said, this is a serious issue, and adequate provisions protecting the freedom of information need to be laid out. As the amount of content on the Semantic Web grows, this issue will become more serious, as it too obeys Metcalfe's Law.</p>
		</div>
	</div>
	<hr>
	<div class="section" id="Progress">
		<h3 class="subsection-title">Progress Towards the Semantic Web</h3>
		<p>When describing it in 2002, Tim described the Semantic Web as "currently in a state comparable to that of hypertext before the advent of the Web: it is clearly a good idea, and some very nice demonstrations exist, but it has not yet changed the world" <a href="#scientific_american">[1]</a>. Though the number of Semantic Web pages is increasing, the majority of webpages do not have Semantic Web content, and the idea has yet to 'change the world' <a href="#semantic_deployment">[35]</a>.</p>

		<p>The sheer amount of content on the Web makes the feasibility of implementing a Knowledge Representation format able to handle all Semantic Content a monumentally difficult task. Many of those who support Semantic Web content choose to do so in restricted domains, avoiding the scaling problems that come with encompassing the Web.</p>
	</div>
	<hr>
	<div class="section" id="Conclusion">
		<h2 class="section-title">Conclusion</h2>
		<p>As content on the Web began to use more and more powerful tools, the ability to automatically analyze that content decreased. The Semantic Web is a response to that complexity. The aim is to make the content on the Web available and understandable again, to not just humans but machines.</p>

		<p>The Semantic Web extends the Web by making machine-exploration and inference possible. On the World Wide Web, URIs can be found in two ways: through a reference on another page, or by human-exploration. On the Semantic Web, in addition to these two methods, dereferencing a URI produces a set of related URIs paired with a description of their relationship to the original URI. This simple modification to the result of a URI dereference gives machine-agents all the information needed to explore the web.</p>

		<p>The difference between the Web as it is now and Tim Berners-Lee's vision for the Semantic Web does not lie in the amount of information online, but in how that information is stored, and how it can be accessed. With two simple ideas - subject-predicate-object metadata in HTML and the inclusion of related URIs on dereference - the Semantic Web changes the nature of the Web and opens up a world opportunity for information exchange.</p> 

		<p>There are many hurdles to overcome before the Web is a Semantic Web, but I believe the value of the Semantic Web far overshadows these obstacles. It isn't a question of whether or not the Semantic Web will exist or not - its a question of when.</p>
	</div>
	<hr>
	<div class="section" id="Bibliography">
		<h2 class="section-title">Bibliography</h2>
		<ol>
			<li class="biblio-ref" id="scientific_american"><a href="http://csis.pace.edu/~marchese/CS835/Lec9/112_SemWeb.pdf">The Semantic Web</a><p> - Tim Berners-Lee, James Hendler and Ora Lassila, Scientific American, 2002.</p></li>
			<li class="biblio-ref" id="rfc_1945_3.5"><a href="http://tools.ietf.org/html/rfc1945#section-3.5">Hypertext Transfer Protocol -- HTTP/1.0</a><p> - T Berners-Lee, R. Fielding, H. Frystyk, EITF, 1996.</p></li>
			<li class="biblio-ref" id="rfc_1945_3.4"><a href="http://tools.ietf.org/html/rfc1945#section-3.4">Hypertext Transfer Protocol -- HTTP/1.0</a><p> - T Berners-Lee, R. Fielding, H. Frystyk, EITF, 1996.</p></li>
			<li class="biblio-ref" id="rfc_3986"><a href="https://tools.ietf.org/html/rfc3986#section-4.5">Uniform Resource Identifier (URI): Generic Syntax</a><p> - T Berners-Lee, R. Fielding, L. Masinter, EITF, 2005.</p></li>
			<li class="biblio-ref" id="www_announcement"><a href="http://archive.wired.com/science/discoveries/news/2007/08/dayintech_0807">Aug. 7, 1991: Ladies and Gentlemen, the World Wide Web</a><p> - Tim Berners-Lee (original post), Tony Long (Wired article author), 2008.</p></li>
			<li class="biblio-ref" id="understanding_web_pages_better"><a href="http://googlewebmastercentral.blogspot.com/2014/05/understanding-web-pages-better.html">Understanding web pages better</a><p> - Erik Hendriks, Michael Xu, Kazushi Nagayama, Google, 2014.</p></li>
			<li class="biblio-ref" id="javascript_announcement"><a href="http://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html">Netscape and Sun announce JavaScript, the Open, Cross-Platform Object Scripting Language for Enterprise Networks and the Internet</a><p> - Netscape Communications, 1995.</p></li>
			<li class="biblio-ref" id="2014_bots"><a href="https://www.incapsula.com/blog/bot-traffic-report-2014.html">2014 Bot Traffic Report: Just the Droids You were Looking for</a><p> - Igal Zeifman, Incapsulata, 2014.</p></li>
			<li class="biblio-ref" id="statistica_internet_time"><a href="http://www.statista.com/statistics/270781/average-daily-media-use-in-the-us/">Average Daily Media Use in the United States from 2010 to 2014 (in minutes)</a><p> - Statistica, 2015.</p></li>
			<li class="biblio-ref" id="wired_iot"><a href="http://www.wired.com/2014/11/the-internet-of-things-bigger/">The Internet of Things Is Far Bigger Than Anyone Realizes</a><p> - Daniel Burrus, Wired Magazine, 2014.</p></li>
			<li class="biblio-ref" id="w3c_semantic_overview"><a href="http://www.w3.org/standards/semanticweb/">Semantic Web</a><p> - W3C.</p></li>
			<li class="biblio-ref" id="tim_linked_data"><a href="http://www.w3.org/DesignIssues/LinkedData.html">Linked Data</a><p> - Tim Berners-Lee, 2006.</p></li>
			<li class="biblio-ref" id="semantic_queries_in_databases"><a href="http://delivery.acm.org/10.1145/1650000/1646157/p1505-lim.pdf?ip=130.64.178.220&amp;id=1646157&amp;acc=ACTIVE%20SERVICE&amp;key=AA86BE8B6928DDC7%2E4579F4D1C4C67060%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&amp;CFID=508424173&amp;CFTOKEN=64210780&amp;__acm__=1430582031_e79258a6a9a6b2a3fcee017d181a319e">Semantic Queries in Databases: Problems and Challenges</a><p> - Lipyeow Lim, Haixun Wang, and Min Wang, ACM, 2009.</p></li>
			<li class="biblio-ref" id="advantages_of_RDF"><a href="http://answers.semanticweb.com/questions/19183/advantages-of-rdf-over-relational-databases">Advantages of RDF over Relational Databases</a><p> - Semantic Web Forum, 2012.</p></li>
			<li class="biblio-ref" id="w3c_vocabularies"><a href="http://www.w3.org/standards/semanticweb/ontology.html">Vocabularies</a><p> - W3C.</p></li>
			<li class="biblio-ref" id="metcalfes_law_semantic"><a href="http://www.cs.umd.edu/~golbeck/downloads/Web20-SW-JWS-webVersion.pdf">Metcalfe's Law, Web 2.0, and the Semantic Web</a><p> - James Hendler and Jennifer Golbeck, University of Maryland, 2008.</p></li>
			<li class="biblio-ref" id="stanford_vagueness"><a href="http://plato.stanford.edu/entries/vagueness/">Vagueness</a><p> - Roy Sorensen, Stanford Encyclopedia of Philosophy, 2013.</p></li>
			<li class="biblio-ref" id="w3c_inference"><a href="http://www.w3.org/standards/semanticweb/inference">Inference</a><p> - W3C.</p></li>
			<li class="biblio-ref" id="logical_inconsistency"><a href="http://sqig.math.ist.utl.pt/pub/MarcosJ/01-cm-ecnsql.pdf">Ex Contradictione Non Sequitur Quodlibet</a><p> - Walter A. Carnielli and Jaoa Marcos, BARK, 2001.</p></li>
			<li class="biblio-ref" id="logical_paraconsistency"><a href="http://plato.stanford.edu/entries/logic-paraconsistent/">Paraconsistent Logic</a><p> - Graham Priest, Koji Tanaka, and Zach Weber, Stanford Encyclopedia of Philosophy, 2015.</p><p></li>
			<li class="biblio-ref" id="defeasible_logic"><a href="http://link.springer.com/chapter/10.1007%2F3-540-36524-9_13?LI=true#page-1">Defeasible Logic</a><p> - Donald Nute, University of Georgia, 2003.</p></li>
			<li class="biblio-ref" id="calculating_uncertainty"><a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&amp;arnumber=6421960">Calculating Semantic Uncertainty</a><p> - Gunther Wirsching, CogInfoCom, 2012.</p></li>
			<li class="biblio-ref" id="fuzzy_logic"><a href="http://www.sfu.ca/~jeffpell/papers/ReviewHajek.pdf">Mathematics of Fuzzy Logic</a><p> - Francis Jeffry Pelletier, 2000.</p></li>
			<li class="biblio-ref" id="w3c_rdfa"><a href="http://www.w3.org/TR/2012/WD-rdfa-in-html-20120329/">HTML+RDFa 1.1</a><p> - Ben Adida, Mark Birbeck and Steven Pemberton, W3C, 2012.</p></li>
			<li class="biblio-ref" id="w3c_rdfa_triples"><a href="http://www.w3.org/TR/2011/WD-rdfa-core-20111215/#triples">RDFa Core 1.1</a><p> - W3C, 2011.</p></li>
			<li class="biblio-ref" id="microformats"><a href="http://microformats.org/wiki/about">About Microformats</a><p> - microformats.org, 2015.</p>
			</li><li class="biblio-ref" id="microdata"><a href="http://googleblog.blogspot.com/2011/06/introducing-schemaorg-search-engines.html">Introducing schema.org: Search engines come together for a richer web</a><p> - Google, 2011.</p></li>
			<li class="biblio-ref" id="w3c_rdfs"><a href="http://www.w3.org/TR/rdf-schema/#ch_introduction">RDF Schema 1.1</a><p> - Dan Brickley and R.V. Guha, W3C, 2014.</p></li>
			<li class="biblio-ref" id="w3c_owl_2"><a href="http://www.w3.org/TR/owl2-overview/">OWL 2 Web Ontology Language Documentation Overview (Second Edition)</a><p> - W3C Owl Working Group, 2012.</p></li>
			<li class="biblio-ref" id="w3c_owl"><a href="http://www.w3.org/TR/2004/REC-owl-features-20040210/">Owl Web Ontology Language Overview</a><p> - Deborah L. McGuinness and Frank van Harmelen, W3C, 2004.</p></li>
			<li class="biblio-ref" id="w3c_skos"><a href="http://www.w3.org/TR/2009/REC-skos-reference-20090818/">SKOS Simple Knowledge Organization System Reference</a><p> - Alistair Miles and Sean Bechhofer, W3C, 2009.</p>
			</li><li class="biblio-ref" id="w3c_sparql"><a href="http://www.w3.org/TR/sparql11-query/">SPARQL 1.1 Query Language</a><p> - Steve Harris, Andy Seaborne, W3C, 2013.</p></li>
			<li class="biblio-ref" id="rif"><a href="http://download-v2.springer.com/static/pdf/24/bok%253A978-3-540-88737-9.pdf?token2=exp=1430600310~acl=%2Fstatic%2Fpdf%2F24%2Fbok%25253A978-3-540-88737-9.pdf*~hmac=57fdfc3216d0446b562094091d637a0ff99b3cb170a61b26041fa6245d312c65">Rule Interchange Format: The Framework</a><p> - Michael Kifer, 2008.</p></li>
			<li class="biblio-ref" id="number_of_webpages"><a href="http://www.worldwidewebsize.com/">The size of the World Wide Web (The Internet)</a><p> - worldwidewebsize.com, 2015.</p></li>
			<li class="biblio-ref" id="semantic_deployment"><a href="http://hannes.muehleisen.org/Bizer-etal-DeploymentRDFaMicrodataMicroformats-ISWC-InUse-2013.pdf">Deployment of RDFa, Microdata, and Microformats on the Web - A Quantitative Analysis</a><p> - Christian Bizer, Kai Eckert, Robert Meusel, Hannes Muhleisen, Michael Schumacher and Johanna Volker, University of Mannheim, 2013.</p></li>
		</ol>
	</div>
</div>
